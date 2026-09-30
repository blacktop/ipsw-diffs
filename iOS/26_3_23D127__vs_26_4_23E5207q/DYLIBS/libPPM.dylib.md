## libPPM.dylib

> `/usr/lib/libPPM.dylib`

```diff

-1035.80.9.0.0
-  __TEXT.__text: 0x11a0
-  __TEXT.__auth_stubs: 0x390
+1035.100.46.0.0
+  __TEXT.__text: 0x11cc
+  __TEXT.__auth_stubs: 0x360
   __TEXT.__objc_methlist: 0x184
   __TEXT.__const: 0xb8
   __TEXT.__cstring: 0x563

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x118
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x1d0
+  __AUTH_CONST.__auth_got: 0x1b8
   __AUTH_CONST.__cfstring: 0x420
   __AUTH_CONST.__objc_const: 0x260
   __DATA.__objc_ivar: 0x18

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 59214E18-3460-3470-ACE8-B4D3441CD51C
+  UUID: F496A38C-5A35-3400-AD56-939D62380650
   Functions: 32
-  Symbols:   180
+  Symbols:   177
   CStrings:  143
 
Symbols:
+ _objc_autoreleaseReturnValue
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x3
Functions:
~ -[PPMClient initWithClientIdentifier:] : 116 -> 108
~ +[PPMClient sharedInstanceWithClientRepresentation:options:error:] : 188 -> 200
~ ___66+[PPMClient sharedInstanceWithClientRepresentation:options:error:]_block_invoke : 168 -> 172
~ -[PPMClient getClientNumber:] : 124 -> 128
~ _budgetNotificationCallback : 344 -> 360
~ -[PPMClient admissionCheckWithLevel:options:error:handler:] : 332 -> 336
~ -[PPMClient activityStoppedWithLevel:options:error:] : 204 -> 208
~ -[PPMClient activityStartedWithLevel:options:error:] : 204 -> 208
~ -[PPMClient pushTelemetryToPPM:error:] : 964 -> 968

```
