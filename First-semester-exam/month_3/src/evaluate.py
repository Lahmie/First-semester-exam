import pandas as pd

class WaterQualityEvaluator:
    def __init__(self, ph_range=(6.5, 8.5), turbidity_threshold=1.0):
        self.ph_range = ph_range
        self.turbidity_threshold = turbidity_threshold

    def get_unsafe_reason(self, row: pd.Series) -> str:
        """
        Determine the reason why a row of water data is unsafe.
        """
        if row['pH'] < self.ph_range[0]:
            return "pH too low"
        elif row['pH'] > self.ph_range[1]:
            return "pH too high"
        elif row['turbidity'] > self.turbidity_threshold:
            return "turbidity too high"
        else:
            return "Safe"
    
    def is_safe(self, row: pd.Series) -> bool:
        """
        Determine if a row of water data is safe.
        """
        return self.get_unsafe_reason(row) is None
    
    def save_results(self, df, output_filepath):
        """Save evaluation results for each recording"""
        
        results = []

        for _, row in df.iterrows():
            is_safe = self.is_safe(row)
            reason = self.get_unsafe_reason(row)
            
            if is_safe:
                result = f"{row['sensor_id']} at {row['timestamp']}: Safe"
            else:
                result = f"{row['sensor_id']} at {row['timestamp']}: Unsafe ({reason})"
            results.append(result)
        
        # Save results to file
        with open(output_filepath, 'w') as f:
            f.write('\n'.join(results))