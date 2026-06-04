def calculate_carbon(requests, avg_response_time_ms, region):
    avg_seconds = avg_response_time_ms / 1000.0
    total_minutes = (requests * avg_seconds) / 60.0
    
    kwh_per_minute = 0.0000167
    total_kwh = total_minutes * kwh_per_minute
    
    grid_intensity = {
        "us-east-1": 379.0,
        "eu-west-1": 282.0,
        "eu-north-1": 12.0
    }
    
    intensity = grid_intensity.get(region, 379.0)
    co2 = total_kwh * intensity
    
    return {
        "kwh": round(total_kwh, 6),
        "co2": round(co2, 4)
    }

print("=" * 50)
print(" GREEN LAMBDA AUDITOR - REPORT ")
print("=" * 50)

fast_reqs, fast_time = 338, 5000.83
heavy_reqs, heavy_time = 108, 6402.34

for reg in ["us-east-1", "eu-west-1", "eu-north-1"]:
    print(f"\n[REGION: {reg.upper()}]")
    
    fast = calculate_carbon(fast_reqs, fast_time, reg)
    heavy = calculate_carbon(heavy_reqs, heavy_time, reg)
    
    total_co2 = fast["co2"] + heavy["co2"]
    total_kwh = fast["kwh"] + heavy["kwh"]
    
    print(f"  /api/fast  -> {fast['co2']}g CO2")
    print(f"  /api/heavy -> {heavy['co2']}g CO2")
    print(f"  >> TOTAL: {round(total_co2, 4)}g CO2 ({round(total_kwh, 5)} kWh)")
print("=" * 50)