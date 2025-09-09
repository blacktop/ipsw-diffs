## Symbolication

> `/System/Library/PrivateFrameworks/Symbolication.framework/Symbolication`

```diff

 64572.137.1.0.0
-  __TEXT.__text: 0xb089c
+  __TEXT.__text: 0xb0b74
   __TEXT.__auth_stubs: 0x2410
-  __TEXT.__objc_methlist: 0x65d0
+  __TEXT.__objc_methlist: 0x65d8
   __TEXT.__const: 0x2b6
-  __TEXT.__cstring: 0xff88
-  __TEXT.__gcc_except_tab: 0x4ebc
+  __TEXT.__cstring: 0xffe8
+  __TEXT.__gcc_except_tab: 0x4ed8
   __TEXT.__oslogstring: 0x17ac
   __TEXT.__ustring: 0x24
   __TEXT.__swift5_typeref: 0x402

   __TEXT.__swift5_reflstr: 0x311
   __TEXT.__swift5_fieldmd: 0x2a8
   __TEXT.__swift5_types: 0x14
-  __TEXT.__unwind_info: 0x2940
+  __TEXT.__unwind_info: 0x2948
   __TEXT.__objc_classname: 0x83a
-  __TEXT.__objc_methname: 0xf440
-  __TEXT.__objc_methtype: 0x5e7d
-  __TEXT.__objc_stubs: 0x9a00
+  __TEXT.__objc_methname: 0xf48f
+  __TEXT.__objc_methtype: 0x5e83
+  __TEXT.__objc_stubs: 0x9a20
   __DATA_CONST.__got: 0x458
   __DATA_CONST.__const: 0x35f8
   __DATA_CONST.__objc_classlist: 0x2d0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3568
+  __DATA_CONST.__objc_selrefs: 0x3570
   __DATA_CONST.__objc_superrefs: 0x200
   __DATA_CONST.__objc_arraydata: 0x870
   __AUTH_CONST.__auth_got: 0x1220
-  __AUTH_CONST.__const: 0x11d8
-  __AUTH_CONST.__cfstring: 0xd860
-  __AUTH_CONST.__objc_const: 0xbcd8
+  __AUTH_CONST.__const: 0x11f8
+  __AUTH_CONST.__cfstring: 0xd8a0
+  __AUTH_CONST.__objc_const: 0xbd38
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x18

   __AUTH.__data: 0x50
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x8
-  __DATA.__objc_ivar: 0xc6c
+  __DATA.__objc_ivar: 0xc78
   __DATA.__data: 0xd58
-  __DATA.__bss: 0x548
+  __DATA.__bss: 0x558
   __DATA.__common: 0xf9
   __DATA_DIRTY.__objc_data: 0x1770
   __DATA_DIRTY.__crash_info: 0x148

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: B56D3CC4-D22E-3EE8-9C00-B455497D34DC
-  Functions: 3120
-  Symbols:   10533
-  CStrings:  7743
+  UUID: 0050EDE5-4EA5-342B-9A8F-6E2EDAAF22EE
+  Functions: 3126
+  Symbols:   10552
+  CStrings:  7753
 
Symbols:
+ -[VMUProcessDescription targetUsesExtraPointerBits:].cold.1
+ -[VMUTask useExtraPointerStripping]
+ -[VMUVMRegion isExtraBits]
+ OBJC_IVAR_$_VMUVMRegion.is_extra_bits
+ _OBJC_IVAR_$_VMUTask._targetUsesExtraBits
+ _OBJC_IVAR_$_VMUTask._targetUsesExtraBitsInitialized
+ __ZZ52-[VMUProcessDescription targetUsesExtraPointerBits:]E41osSecurityConfigGetForTaskFunctionPointer
+ __ZZ52-[VMUProcessDescription targetUsesExtraPointerBits:]E9onceToken
+ ___52-[VMUProcessDescription targetUsesExtraPointerBits:]_block_invoke
+ ___block_literal_global.138
+ _objc_msgSend$targetUsesExtraPointerBits:
Functions:
~ _getRegionData : 844 -> 880
+ -[VMUTask useExtraPointerStripping]
+ _OUTLINED_FUNCTION_2
~ _OUTLINED_FUNCTION_0 : 12 -> 16
~ -[VMUProcessDescription targetUsesExtraPointerBits:] : 88 -> 180
+ ___52-[VMUProcessDescription targetUsesExtraPointerBits:]_block_invoke
~ -[VMUProcessDescription processDescriptionHeader] : 1320 -> 1436
+ _OUTLINED_FUNCTION_1
~ -[VMUVMRegion initWithVMRegionData:encodedVersion:simpleSerializer:error:] : 784 -> 792
~ -[VMUVMRegion setVMRegionAttributeStatusData:] : 44 -> 60
~ -[VMUVMRegion getVMRegionData:withSimpleSerializer:] : 368 -> 388
~ -[VMUVMRegion getVMRegionAttributeStatusData:] : 40 -> 64
~ -[VMUVMRegion descriptionWithOptions:maximumLength:memorySizeDivisor:hasFractionalPageSizes:] : 2684 -> 2720
+ -[VMUVMRegion isExtraBits]
~ -[VMUVMRegion breakAtLength:] : 432 -> 440
~ ___maxAttributesWidth_block_invoke : 168 -> 180
+ -[VMUProcessDescription targetUsesExtraPointerBits:].cold.1
~ -[VMUTask ptrauthStripDataPointer:] : 28 -> 72
~ -[VMUTask ptrauthStripFunctionPointer:] : 28 -> 60
~ -[VMUTask stripExtraPointerBits:] : 36 -> 76
CStrings:
+ " %@ %@ %@  "
+ " (MTE Enabled)"
+ "/usr/lib/system/libsystem_platform.dylib"
+ "@48@0:8^{_VMUVMRegionData=QQIiiIIIIIiICCCIIb1b1b1b1b1b1b1b1b24QQQQQQQ}16q24@32^@40"
+ "MTE"
+ "_targetUsesExtraBits"
+ "_targetUsesExtraBitsInitialized"
+ "b24"
+ "isExtraBits"
+ "is_extra_bits"
+ "os_security_config_get_for_task"
+ "v24@0:8^{_VMUVMRegionAttributeStatusData=b1b1b1b13}16"
+ "v32@0:8^{_VMUVMRegionData=QQIiiIIIIIiICCCIIb1b1b1b1b1b1b1b1b24QQQQQQQ}16@24"
- " %@ %@  "
- "@48@0:8^{_VMUVMRegionData=QQIiiIIIIIiICCCIIb1b1b1b1b1b1b1b25QQQQQQQ}16q24@32^@40"
- "b25"
- "v24@0:8^{_VMUVMRegionAttributeStatusData=b1b1b14}16"
- "v32@0:8^{_VMUVMRegionData=QQIiiIIIIIiICCCIIb1b1b1b1b1b1b1b25QQQQQQQ}16@24"

```
