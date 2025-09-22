## libAONConnection.dylib

> `/usr/lib/libAONConnection.dylib`

```diff

-123.0.6.0.0
-  __TEXT.__text: 0x7ac0
-  __TEXT.__auth_stubs: 0x690
-  __TEXT.__const: 0x178
-  __TEXT.__cstring: 0x1605
-  __TEXT.__gcc_except_tab: 0xec
-  __TEXT.__oslogstring: 0x757
-  __TEXT.__unwind_info: 0x218
+123.40.2.0.0
+  __TEXT.__text: 0x8238
+  __TEXT.__auth_stubs: 0x6e0
+  __TEXT.__const: 0x188
+  __TEXT.__cstring: 0x166d
+  __TEXT.__gcc_except_tab: 0x164
+  __TEXT.__oslogstring: 0x89f
+  __TEXT.__unwind_info: 0x258
   __TEXT.__objc_classname: 0x1
-  __DATA_CONST.__got: 0x50
-  __DATA_CONST.__const: 0x3c0
+  __TEXT.__objc_methname: 0x8c
+  __TEXT.__objc_stubs: 0x60
+  __DATA_CONST.__got: 0x58
+  __DATA_CONST.__const: 0x3e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __AUTH_CONST.__auth_got: 0x350
-  __AUTH_CONST.__const: 0x160
-  __AUTH_CONST.__cfstring: 0x20
+  __DATA_CONST.__objc_selrefs: 0x18
+  __AUTH_CONST.__auth_got: 0x380
+  __AUTH_CONST.__const: 0x180
+  __AUTH_CONST.__cfstring: 0xa0
   __DATA.__data: 0x40
-  __DATA.__bss: 0x30
+  __DATA.__bss: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5A6E7B16-C913-30C9-92B5-1013B02833B6
-  Functions: 132
-  Symbols:   399
-  CStrings:  147
+  UUID: 9C0F4243-A0D3-346D-8473-3864944D9E8E
+  Functions: 134
+  Symbols:   421
+  CStrings:  172
 
Symbols:
+ GCC_except_table29
+ GCC_except_table37
+ GCC_except_table40
+ GCC_except_table49
+ GCC_except_table56
+ GCC_except_table58
+ _OBJC_CLASS_$_SDRDiagnosticReporter
+ __ZL19aon_net_log_buffersPKtjPKc
+ __ZL20debug_num_tx_buffers
+ __ZZL27trigger_abc_for_buffer_lossvE27symptom_diagnostic_reporter
+ ____ZL27trigger_abc_for_buffer_lossv_block_invoke
+ ___aon_net_service_init_block_invoke.19
+ ___aon_net_service_init_block_invoke.20
+ ___block_descriptor_32_e22_v16?0"NSDictionary"8l
+ ___block_literal_global.44
+ ___block_literal_global.49
+ _objc_alloc
+ _objc_msgSend
+ _objc_msgSend$initWithQueue:
+ _objc_msgSend$signatureWithDomain:type:subType:detectedProcess:triggerThresholdValues:
+ _objc_msgSend$snapshotWithSignature:duration:event:payload:reply:
+ _objc_release_x21
+ _objc_release_x22
+ _objc_release_x25
+ _objc_retain_x1
- GCC_except_table38
- GCC_except_table43
- ___aon_net_service_init_block_invoke.17
- ___aon_net_service_init_block_invoke_6
- ___block_literal_global.29
CStrings:
+ "%s: [%u-%u/%u] [%s]"
+ "%u%s"
+ ", "
+ "Channel"
+ "Failed to send snapshot to Symptoms"
+ "Leak"
+ "Successfully sent snapshot to Symptoms"
+ "ULPN"
+ "aon_net_service_destroy"
+ "aop2->ap complete buffers"
+ "ap->aop2 submit buffers"
+ "apsd"
+ "got response from diagnosticReporter %@"
+ "initWithQueue:"
+ "signatureWithDomain:type:subType:detectedProcess:triggerThresholdValues:"
+ "snapshotWithSignature:duration:event:payload:reply:"
+ "tx alloced buf %u free %u expected free %u"
+ "tx channel init numFree %u"
+ "tx complete %u buffers numFree %u expected %u"
+ "tx dealloc buf %u status %d free %u expected free %u"
+ "v16@?0@\"NSDictionary\"8"

```
