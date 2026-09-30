## ClockComplications

> `/System/Library/PrivateFrameworks/ClockComplications.framework/ClockComplications`

```diff

-2483.340.22.27.0
-  __TEXT.__text: 0xdfc
-  __TEXT.__auth_stubs: 0x1d0
+2483.340.58.2.0
+  __TEXT.__text: 0xe38
+  __TEXT.__auth_stubs: 0x1b0
   __TEXT.__objc_methlist: 0x40c
   __TEXT.__const: 0x48
   __TEXT.__cstring: 0xad

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x258
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0xf0
+  __AUTH_CONST.__auth_got: 0xe0
   __AUTH_CONST.__cfstring: 0xa0
   __AUTH_CONST.__objc_const: 0x6d8
   __AUTH.__objc_data: 0x140

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 759B6A35-307B-3109-B7C0-0CE83002484F
+  UUID: 21816400-FB18-314F-9AE0-359CC546BB51
   Functions: 75
-  Symbols:   280
+  Symbols:   278
   CStrings:  151
 
Symbols:
+ _objc_release_x23
+ _objc_retain
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_release_x25
- _objc_retain_x2
- _objc_retain_x24
- _objc_retain_x3
Functions:
~ +[CLKCComplicationBundleDataSource bundleIdentifier] : 88 -> 96
~ -[CLKCComplicationBundleDataSource complicationDescriptor] : 160 -> 172
~ -[CLKCComplicationBundleDataSource getLaunchURLForTimelineEntryDate:timeTravelDate:withHandler:] : 240 -> 256
~ +[CLKCBundleComplication complicationWithBundleIdentifier:appBundleIdentifier:complicationDescriptor:] : 132 -> 124
~ +[CLKCBundleComplication complicationWithBundleIdentifier:appBundleIdentifier:] : 116 -> 112
~ -[CLKCBundleComplication initWithBundleIdentifier:appBundleIdentifier:complicationDescriptor:] : 216 -> 212
~ -[CLKCBundleComplication description] : 188 -> 204
~ -[CLKCBundleComplication isEqual:] : 264 -> 268
~ -[CLKCBundleComplication hash] : 96 -> 104
~ -[CLKCBundleComplication initWithCoder:] : 264 -> 276
~ -[CLKCBundleComplication encodeWithCoder:] : 152 -> 160
~ -[CLKCComplicationDataSource initWithComplication:family:forDevice:] : 184 -> 176

```
