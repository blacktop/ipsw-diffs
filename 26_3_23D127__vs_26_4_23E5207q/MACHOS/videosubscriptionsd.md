## videosubscriptionsd

> `/usr/libexec/videosubscriptionsd`

```diff

-593.30.1.0.0
-  __TEXT.__text: 0xb4a8
-  __TEXT.__auth_stubs: 0x500
+593.40.5.0.0
+  __TEXT.__text: 0xb8bc
+  __TEXT.__auth_stubs: 0x4c0
   __TEXT.__objc_stubs: 0x20e0
   __TEXT.__objc_methlist: 0x6c0
   __TEXT.__const: 0x60
-  __TEXT.__gcc_except_tab: 0x2d8
+  __TEXT.__gcc_except_tab: 0x2c0
   __TEXT.__objc_methname: 0x1f98
-  __TEXT.__oslogstring: 0x1296
+  __TEXT.__oslogstring: 0x1464
   __TEXT.__cstring: 0x6d2
   __TEXT.__objc_classname: 0xc3
   __TEXT.__objc_methtype: 0x5ab
-  __TEXT.__unwind_info: 0x310
-  __DATA_CONST.__auth_got: 0x290
+  __TEXT.__unwind_info: 0x360
+  __DATA_CONST.__auth_got: 0x270
   __DATA_CONST.__got: 0x250
   __DATA_CONST.__const: 0x760
   __DATA_CONST.__cfstring: 0x360

   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1BA50DB7-02D6-3701-97E8-BF6AFA738D91
-  Functions: 235
-  Symbols:   168
-  CStrings:  584
+  UUID: 563EFC0B-1F0D-3C9A-80BF-52042C9A4FB0
+  Functions: 245
+  Symbols:   164
+  CStrings:  590
 
Symbols:
+ _objc_retain_x27
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x5
- _objc_retain_x6
CStrings:
+ "Failed to initialize VSUserAccountPersistentContainer! Registry cannot function without Core Data."
+ "Failed to initialize VSUserAccountRegistry! Service cannot function without registry."
+ "Successfully initialized VSUserAccountPersistentContainer"
+ "Successfully initialized VSUserAccountRegistry"
+ "This indicates Core Data initialization failed. The service will be non-functional."
+ "This indicates a serious issue with Core Data model loading or framework bundle access."

```
