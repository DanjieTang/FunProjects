import Foundation
import CoreML

// Load configuration for this ml model
let config: MLModelConfiguration = MLModelConfiguration()
config.computeUnits = .cpuAndNeuralEngine

// Load the model
let model = try HuggingFace_ane_transformers_distilbert_seqLen128_batchSize1(configuration: config)

// Prepare input
let shape: [NSNumber] = [1, 128]
guard let mlMultiArray: MLMultiArray = try? MLMultiArray(shape: shape, dataType: .float32) else {
    fatalError("Couldn't create MLMultiArray")
}

for i in 0..<mlMultiArray.count {
    mlMultiArray[i] = NSNumber(value: Float(i))
}

let input = HuggingFace_ane_transformers_distilbert_seqLen128_batchSize1Input(input_input_ids: mlMultiArray, input_attention_mask: mlMultiArray)

// Testing how long does it take to run 10000 times
let startTime: Date = Date()
for i in 0...10000{
    let output: HuggingFace_ane_transformers_distilbert_seqLen128_batchSize1Output = try model.prediction(input: input)
}
let endTime: Date = Date()

// Display time elapsed
let timeElapsed: TimeInterval = endTime.timeIntervalSince(startTime)
print("Time elapsed: \(timeElapsed) seconds")
