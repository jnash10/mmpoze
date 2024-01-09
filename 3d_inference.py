from mmpose.apis import MMPoseInferencer

# build the inferencer with 3d model alias
inferencer = MMPoseInferencer(pose3d="human3d")

img_path = "steve.jpg"

result_generator = inferencer(img_path, out_dir="predictions")
result = next(result_generator)

print(result)
