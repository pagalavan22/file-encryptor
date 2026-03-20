from datetime import datetime
import os

def generate_report(actions):
    """Generate HTML report of all encryption actions."""

    rows = ""
    for a in actions:
        color = "#44bb44" if a["action"] == "Encrypted" else "#4488ff"
        rows += (
            "<tr>"
            f"<td>{a['file']}</td>"
            f"<td style='color:{color};font-weight:600'>{a['action']}</td>"
            f"<td>{a['time']}</td>"
            f"<td>{a['size']}</td>"
            f"<td style='color:{'#ffaa00' if a['shredded'] else '#888'}'>"
            f"{'Yes' if a['shredded'] else 'No'}</td>"
            "</tr>"
        )

    html = (
        "<!DOCTYPE html><html><head>"
        "<meta charset='UTF-8'>"
        "<title>Encryption Report</title>"
        "<style>"
        "body{font-family:'Segoe UI',sans-serif;background:#0d1117;"
        "color:#c9d1d9;margin:0;padding:30px}"
        "h1{color:#58a6ff}"
        ".meta{background:#161b22;padding:16px;border-radius:8px;"
        "margin-bottom:24px;border:1px solid #30363d}"
        ".meta span{color:#58a6ff;font-weight:600}"
        "table{width:100%;border-collapse:collapse;"
        "background:#161b22;border-radius:8px}"
        "th{background:#21262d;padding:12px 16px;text-align:left;"
        "color:#58a6ff;font-size:12px;text-transform:uppercase}"
        "td{padding:12px 16px;border-top:1px solid #21262d;font-size:14px}"
        ".footer{margin-top:24px;font-size:12px;color:#555}"
        "</style></head><body>"
        "<h1>🔐 Encryption Report</h1>"
        "<div class='meta'>"
        f"<p>Generated: <span>{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</span></p>"
        f"<p>Total Actions: <span>{len(actions)}</span></p>"
        "</div>"
        "<table><tr>"
        "<th>File</th><th>Action</th><th>Time</th>"
        "<th>Size</th><th>Shredded</th>"
        "</tr>"
        + (rows if rows else
           "<tr><td colspan='5' style='text-align:center;color:#555;"
           "padding:24px'>No actions recorded</td></tr>")
        + "</table>"
        "<div class='footer'>File Encryption Tool v3.0</div>"
        "</body></html>"
    )
    return html