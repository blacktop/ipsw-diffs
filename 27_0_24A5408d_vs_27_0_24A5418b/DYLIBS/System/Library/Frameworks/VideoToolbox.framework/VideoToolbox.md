## VideoToolbox

> `/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-3350.75.2.0.0
+3350.77.1.6.0
   __TEXT.__text: 0x5399e8
   __TEXT.__delay_helper: 0xdc
   __TEXT.__objc_methlist: 0xefc
Functions:
~ _vtCompressionSessionCompressionWork : 5344 -> 5340
~ -[VTLowLatencySuperResolutionScalerConfiguration initWithFrameWidth:frameHeight:scaleFactor:] : 252 -> 256
~ sub_18ecfa818 -> sub_18ecfc818 : 380 -> 392
~ sub_18ecfa994 -> sub_18ecfc9a0 : 392 -> 380
CStrings:
+ "description=CoreMedia_VideoToolbox-3350.77.1.6"
- "description=CoreMedia_VideoToolbox-3350.75.2"
```
