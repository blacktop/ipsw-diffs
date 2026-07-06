## libSEUpdater.dylib

> `/usr/lib/updaters/libSEUpdater.dylib`

```diff

-  __TEXT.__text: 0x72774
+  __TEXT.__text: 0x72608
   __TEXT.__init_offsets: 0x20
   __TEXT.__objc_methlist: 0x654
   __TEXT.__const: 0xa5dc
   __TEXT.__oslogstring: 0x5e
-  __TEXT.__cstring: 0x8e81
-  __TEXT.__gcc_except_tab: 0x8518
-  __TEXT.__unwind_info: 0x1d08
+  __TEXT.__cstring: 0x8eab
+  __TEXT.__gcc_except_tab: 0x857c
+  __TEXT.__unwind_info: 0x1d18
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5a8
+  __DATA_CONST.__const: 0x588
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x610
+  __DATA_CONST.__objc_selrefs: 0x620
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__got: 0x200
+  __DATA_CONST.__got: 0x208
   __AUTH_CONST.__const: 0x4588
   __AUTH_CONST.__cfstring: 0x2320
   __AUTH_CONST.__objc_const: 0x8f0

   - /usr/lib/libnfrestore.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 1577
-  Symbols:   5092
-  CStrings:  1565
+  Symbols:   5093
+  CStrings:  1564
 
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ GCC_except_table125
+ GCC_except_table142
+ GCC_except_table193
+ GCC_except_table197
+ GCC_except_table201
+ GCC_except_table207
+ GCC_except_table80
+ GCC_except_table88
+ __GLOBAL__sub_I_P73BaseUpdateController.mm
+ __ZNSt3__128__exception_guard_exceptionsIZNS_10shared_ptrIN13SEUpdaterUtil5ErrorEEC1B9fqe220106IS3_ZN3ctu20SharedSynchronizableIS3_E15make_shared_ptrIS3_EENS1_IT_EEPSA_EUlPS3_E_Li0EEESC_T0_EUlvE_ED2B9fqe220106Ev
+ ___block_descriptor_48_ea8_32r_e5_v8?0lr32l8
+ _objc_msgSend$numberWithUnsignedLong:
+ _objc_msgSend$unsignedIntValue
- GCC_except_table158
- GCC_except_table196
- GCC_except_table198
- GCC_except_table89
- __GLOBAL__sub_I_P73BaseUpdateController.cpp
- __ZNK9SEUpdater20UpdateControllerBase20usesPORSecureElementEj
CStrings:
+ "Existing packageAID %s anyPackageOutOfDate %d wouldDowngrade %d anyModuleMissing %d, migrationTrigger %s"
+ "RSN 0x%X BSN 0x%X, skipSLAM %d forceSLAM %d isDowngrade %d\n"
+ "chipID 0x%X isProd %d expectedBSN 0x%X (has_value %d) deliveryBSN 0x%X isPORUpdate %d\n"
+ "expectedBSN"
- "Krypton Load and install SLAM"
- "RSN 0x%X BSN 0x%X, skipSLAM %d forceSLAM %d\n"
- "SLAMLoadAndInstallKrypton_3_2_4_0H_eosv2"
- "Skip SE-SEP pairing verification due to non-POR SE 0x%02X\n"
- "Skip personalization due to non-POR SE 0x%02X\n"

```
