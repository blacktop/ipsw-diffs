## SignpostCollection

> `/System/Library/PrivateFrameworks/SignpostCollection.framework/Versions/A/SignpostCollection`

```diff

-146.2.0.0.0
-  __TEXT.__text: 0x7698
-  __TEXT.__auth_stubs: 0x430
+151.7.0.0.0
+  __TEXT.__text: 0x7764
+  __TEXT.__auth_stubs: 0x420
   __TEXT.__objc_methlist: 0x394
-  __TEXT.__const: 0xb8
-  __TEXT.__gcc_except_tab: 0x310
-  __TEXT.__cstring: 0xa07
+  __TEXT.__const: 0x128
+  __TEXT.__gcc_except_tab: 0x330
+  __TEXT.__cstring: 0xa33
   __TEXT.__oslogstring: 0x2d6
-  __TEXT.__unwind_info: 0x220
+  __TEXT.__unwind_info: 0x228
   __TEXT.__objc_classname: 0xbe
-  __TEXT.__objc_methname: 0x1c97
+  __TEXT.__objc_methname: 0x1c8e
   __TEXT.__objc_methtype: 0x22e
-  __TEXT.__objc_stubs: 0x1f00
-  __DATA_CONST.__got: 0x100
+  __TEXT.__objc_stubs: 0x1ee0
+  __DATA_CONST.__got: 0xe8
   __DATA_CONST.__const: 0x88
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x860
+  __DATA_CONST.__objc_selrefs: 0x858
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x228
+  __AUTH_CONST.__auth_got: 0x220
   __AUTH_CONST.__const: 0x420
-  __AUTH_CONST.__cfstring: 0x6e0
+  __AUTH_CONST.__cfstring: 0x700
   __AUTH_CONST.__objc_const: 0x548
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x34

   - /System/Library/PrivateFrameworks/ktrace.framework/Versions/A/ktrace
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FC056ACC-F0C8-3215-AA98-2EDCBA97BB24
-  Functions: 147
-  Symbols:   591
+  UUID: 735ABD4D-B1A6-33CC-A638-746F71DC86F7
+  Functions: 151
+  Symbols:   595
   CStrings:  485
 
Symbols:
+ +[SignpostSupportMachTimeTranslator(Collection) _globalNotificationDispatchQueue].cold.1
+ +[SignpostSupportMachTimeTranslator(Collection) _timeTranslationLog].cold.1
+ SignpostSystemTimebaseRatio.cold.1
+ __153-[SignpostSupportObjectExtractor(Notifications) processNotificationsWithIntervalTimeoutInSeconds:shouldCalculateAnimationFramerate:targetQueue:errorOut:]_block_invoke.32
+ __153-[SignpostSupportObjectExtractor(Notifications) processNotificationsWithIntervalTimeoutInSeconds:shouldCalculateAnimationFramerate:targetQueue:errorOut:]_block_invoke.36
+ __153-[SignpostSupportObjectExtractor(Notifications) processNotificationsWithIntervalTimeoutInSeconds:shouldCalculateAnimationFramerate:targetQueue:errorOut:]_block_invoke.6
+ ___block_descriptor_58_e8_32s40r48r_e23_B16?0^{ktrace_chunk=}8l
+ _objc_msgSend$_checkProcessingConfiguration
+ _objc_msgSend$initWithArgumentObject:scalarType:typeNamespace:type:tokens:stringPrefix:privacy:
+ _objc_msgSend$scalarType
+ _signpostcollection_debug_log.cold.1
- __153-[SignpostSupportObjectExtractor(Notifications) processNotificationsWithIntervalTimeoutInSeconds:shouldCalculateAnimationFramerate:targetQueue:errorOut:]_block_invoke.10
- __153-[SignpostSupportObjectExtractor(Notifications) processNotificationsWithIntervalTimeoutInSeconds:shouldCalculateAnimationFramerate:targetQueue:errorOut:]_block_invoke.35
- __153-[SignpostSupportObjectExtractor(Notifications) processNotificationsWithIntervalTimeoutInSeconds:shouldCalculateAnimationFramerate:targetQueue:errorOut:]_block_invoke.39
- ___block_descriptor_42_e8_32s_e23_B16?0^{ktrace_chunk=}8l
- ___stderrp
- _fprintf
- _objc_msgSend$_hasProcessingBlock
- _objc_msgSend$_processingStarting
- _objc_msgSend$initWithArgumentObject:typeNamespace:type:tokens:stringPrefix:privacy:
- _objc_msgSend$localizedDescription
CStrings:
+ "Could not process trace file '%@' due to unknown error"
+ "_checkProcessingConfiguration"
+ "initWithArgumentObject:scalarType:typeNamespace:type:tokens:stringPrefix:privacy:"
+ "scalarType"
- "ERROR: %s\n"
- "_hasProcessingBlock"
- "_processingStarting"
- "initWithArgumentObject:typeNamespace:type:tokens:stringPrefix:privacy:"
- "localizedDescription"

```
