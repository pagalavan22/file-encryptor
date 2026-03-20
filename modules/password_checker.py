from zxcvbn import zxcvbn

def check_password(password):
    """Check password strength using zxcvbn."""
    result = zxcvbn(password)
    score  = result["score"]  # 0 to 4

    levels = {
        0: ("Very Weak",  "❌", "#ff4444"),
        1: ("Weak",       "⚠️",  "#ff8800"),
        2: ("Fair",       "🔶", "#ffaa00"),
        3: ("Strong",     "✅", "#44bb44"),
        4: ("Very Strong","🔐", "#00cc44"),
    }

    label, icon, color = levels[score]

    feedback = []
    if result["feedback"]["warning"]:
        feedback.append(result["feedback"]["warning"])
    for tip in result["feedback"]["suggestions"]:
        feedback.append(tip)

    crack_time = result["crack_times_display"][
        "offline_slow_hashing_1e4_per_second"
    ]

    return {
        "score":      score,
        "label":      label,
        "icon":       icon,
        "color":      color,
        "crack_time": crack_time,
        "feedback":   feedback
    }