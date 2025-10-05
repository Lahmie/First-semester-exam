from load_data import load_csv
from clean_data import clean_sensor_data
from evaluate import WaterQualityEvaluator

def main():
    # Load data
    input_filepath = '../data/sensor_data.csv'
    data = load_csv(input_filepath)

    
    if data.empty:
        print("No data to process.")
        return

    # Clean data
    clean_data = clean_sensor_data(data)
    
    
    # Evaluate water quality
    evaluator = WaterQualityEvaluator()
  
    # Save results
    output_filepath = '../data/evaluation_results.csv'
    evaluator.save_results(clean_data, output_filepath)

if __name__ == "__main__":
    main()    