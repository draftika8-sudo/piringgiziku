"""
Utility untuk format dan kalkulasi statistik deteksi
"""


def format_detection_stats(stats):
    """
    Format raw detection statistics
    
    Args:
        stats: Dictionary dari detection results
        
    Returns:
        Dictionary dengan formatted statistics (count, avg_confidence, confidences)
    """
    formatted_stats = {}
    
    for cls_name, confidences in stats.items():
        avg_conf = sum(confidences) / len(confidences) if confidences else 0
        formatted_stats[cls_name] = {
            "count": len(confidences),
            "avg_confidence": avg_conf,
            "confidences": confidences
        }
    
    return formatted_stats


def calculate_total_stats(detection_stats):
    """
    Hitung total objek dan rata-rata confidence
    
    Args:
        detection_stats: Formatted detection statistics
        
    Returns:
        tuple: (total_objects, avg_confidence)
    """
    if not detection_stats:
        return 0, 0
    
    total_objects = sum(
        detection_stats.get(cls, {}).get("count", 0) 
        for cls in ["makanan_pokok", "lauk_pauk", "sayur", "buah"]
    )
    
    avg_confidence = 0
    if total_objects > 0:
        total_conf = sum(
            sum(detection_stats.get(cls, {}).get("confidences", [])) 
            for cls in ["makanan_pokok", "lauk_pauk", "sayur", "buah"]
        )
        avg_confidence = total_conf / total_objects
    
    return total_objects, avg_confidence
