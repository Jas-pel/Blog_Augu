
import re
import json

def process_journal(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    terms = []
    current_term = None
    current_post = None
    
    # Precise patterns
    # Terms are usually on their own line
    term_pattern = r'^(1st term|2nd term|3rd term|4th \(and last\) term|First year|Second year|Été)$'
    date_pattern = r'^(\d{1,2}\s+(?:janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre)\s+202\d|25 août 2023|1er septembre 2023)'
    page_num_pattern = r'^\s*\d{1,3}\s*$'
    
    content_started = False

    for line in lines:
        line = line.strip()
        if not line: continue
        
        # Clean form feeds
        line = line.replace('\x0c', '').strip()
        if not line: continue

        # Ignore page numbers
        if re.match(page_num_pattern, line):
            continue

        # Start content at First Page
        if "1st term" in line and "...." not in line:
            content_started = True

        if not content_started:
            continue

        # Term Detection
        if re.match(term_pattern, line, re.IGNORECASE):
            if current_post and current_term:
                current_term['posts'].append(current_post)
                current_post = None
                
            current_term = {"name": line, "posts": []}
            terms.append(current_term)
            continue

        # Date Detection
        date_match = re.match(date_pattern, line)
        if date_match and (line.endswith(':') or len(line) < 50):
            if current_post and current_term:
                current_term['posts'].append(current_post)
            
            date_str = date_match.group(1)
            title = line.replace(date_str, '').replace(':', '').strip()
            current_post = {
                "date": date_str,
                "title": title if title else None,
                "content": []
            }
            continue

        # Content
        if current_post:
            # Fix common PDF artifacts (hyphenation)
            if line.endswith('-'):
                current_post['content'].append(line[:-1])
            else:
                current_post['content'].append(line + " ")

    # Add last post
    if current_post and current_term:
        current_term['posts'].append(current_post)

    # Clean up empty terms or fix hierarchy
    # Some posts might have been assigned to "First year" then another term starts.
    # We want a flat list of sections or a nested one?
    # Let's keep it simple: any non-empty term stays.
    
    final_data = []
    for t in terms:
        if t['posts']:
            # Join content lines into paragraphs
            for p in t['posts']:
                text = "".join(p['content']).strip()
                # Split by emojis or double spaces often used as paragraph markers in this text
                # Or just keep it as one block for now and let CSS handle readability.
                p['content'] = text
            final_data.append(t)

    return final_data

if __name__ == "__main__":
    result = process_journal(r"c:\Kingston\Prog\Blog_Augu\UWC Journal pour imprimer.txt")
    
    with open(r"c:\Kingston\Prog\Blog_Augu\docs\data.js", "w", encoding="utf-8") as f:
        f.write("const blogData = ")
        json.dump(result, f, ensure_ascii=False, indent=2)
        f.write(";\n\nexport default blogData;")
    
    print(f"Processed {len(result)} sections and saved to data.js")
