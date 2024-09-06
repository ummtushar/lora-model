import replicate

def output_img(input):

    output = replicate.run(
        "ummtushar/pilot:52f05e1539387ca36fe0e4eebc688b743a3d2bc2f202936afa5b2a6720ac905e",
        input={
            "prompt": input, 
            "num_inference_steps": 28,
            "guidance_scale": 3.5,
            "model": "dev",
            "aspect_ratio": "2:3",
            "output_format": "png",
        }
    )

    return output

    # print(f"Generated image URL: {output}")

# if __name__ == "__main__":
#     output_img()

