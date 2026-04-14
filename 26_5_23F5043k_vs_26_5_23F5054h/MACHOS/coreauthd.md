## coreauthd

> `filesystem/System/Library/Frameworks/LocalAuthentication.framework/Support/coreauthd`

```diff

-2005.120.8.0.0
-  __TEXT.__text: 0x390dc
+2005.120.17.0.0
+  __TEXT.__text: 0x39198
   __TEXT.__auth_stubs: 0xe00
-  __TEXT.__objc_stubs: 0x3680
+  __TEXT.__objc_stubs: 0x3720
   __TEXT.__objc_methlist: 0x195c
   __TEXT.__const: 0x13d8
-  __TEXT.__objc_methname: 0x4628
+  __TEXT.__objc_methname: 0x467a
   __TEXT.__cstring: 0x4e2b
   __TEXT.__objc_classname: 0x6ef
   __TEXT.__objc_methtype: 0x1e93

   __TEXT.__oslogstring: 0x1655
   __TEXT.__unwind_info: 0xcb8
   __DATA_CONST.__auth_got: 0x710
-  __DATA_CONST.__got: 0x590
+  __DATA_CONST.__got: 0x5a0
   __DATA_CONST.__auth_ptr: 0x30
   __DATA_CONST.__const: 0x20c8
   __DATA_CONST.__cfstring: 0xd00

   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_intobj: 0x30
   __DATA.__objc_const: 0x7840
-  __DATA.__objc_selrefs: 0x1140
+  __DATA.__objc_selrefs: 0x1158
   __DATA.__objc_ivar: 0x170
   __DATA.__objc_data: 0x9b0
   __DATA.__data: 0x1b30

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 045E753D-728D-3938-853F-60C40A4081D8
+  UUID: ADDE5692-C013-3550-A5D0-12929109D40B
   Functions: 1527
-  Symbols:   415
-  CStrings:  1917
+  Symbols:   417
+  CStrings:  1920
 
Symbols:
+ _OBJC_CLASS_$_LACAutoLockStrictModeAdapter
+ _OBJC_CLASS_$_LACDTOAnalyticsProcessor
+ _OBJC_CLASS_$_LACDTOAnalyticsProcessorLocation
- _OBJC_CLASS_$_LACDTOAnalyticsProcessorFactory
Functions:
~ sub_100003220 : 432 -> 556
~ sub_100011c0c -> sub_100011c88 : 1208 -> 1272
CStrings:
+ "featureFlagDimpleKeyiPadTelemetryEnabled"
+ "initWithAnalyticsReporting:"
+ "initWithAnalyticsReporting:locationProvider:"
+ "initWithFeatureStateProvider:"
+ "makeAutoLockServiceWithContextProvider:strictModeAdapter:"
- "makeAutoLockServiceWithContextProvider:"
- "processorWithAnalyticsReporting:locationProvider:deviceFamilyInfo:featureFlags:"

```
