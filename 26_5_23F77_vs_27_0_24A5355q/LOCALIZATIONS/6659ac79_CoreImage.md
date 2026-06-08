## CoreImage

> `FileSystem/System/Library/Frameworks/CoreImage.framework/Descriptions.loctable`

```diff

 en.CISaturationBlendMode.inputImage = "The image to use as a foreground image."
 en.CIScreenBlendMode = "Multiplies the inverse of the source image samples with the inverse of the background image samples. This results in colors that are at least as light as either of the two contributing sample colors."
 en.CIScreenBlendMode.inputImage = "The image to use as a foreground image."
+en.CISeimensStarGenerator = "Generates a Siemens star pattern with alternating color spokes radiating from a center point. The output is typically used as a test pattern or design element."
+en.CISeimensStarGenerator.inputAngle = "The angle in radians of the pattern."
+en.CISeimensStarGenerator.inputCenter = "The center of the star pattern."
+en.CISeimensStarGenerator.inputColor0 = "The color of the first set of spokes."
+en.CISeimensStarGenerator.inputColor1 = "The color of the second set of spokes."
+en.CISeimensStarGenerator.inputCount = "The number of alternating color spokes. Values range from 2 to 64."
+en.CISeimensStarGenerator.inputRadius = "The radius of the star pattern."
 en.CISepiaTone = "Maps the colors of an image to various shades of brown."
 en.CISepiaTone.inputIntensity = "The intensity of the sepia effect. A value of 1.0 creates a monochrome sepia image. A value of 0.0 has no effect on the image."
 en.CIShadedMaterial = "Produces a shaded image from a height field. The height field is defined to have greater heights with lighter shades, and lesser heights (lower areas) with darker shades. You can combine this filter with the “Height Field From Mask” filter to produce quick shadings of masks, such as text."

```
