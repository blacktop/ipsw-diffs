## NanoPassKit

> `/System/Library/PrivateFrameworks/NanoPassKit.framework/NanoPassKit`

```diff

-1163.14.2.0.0
-  __TEXT.__text: 0x213bf4
+1163.17.0.0.0
+  __TEXT.__text: 0x213c3c
   __TEXT.__auth_stubs: 0x17e0
-  __TEXT.__objc_methlist: 0x204fc
+  __TEXT.__objc_methlist: 0x2052c
   __TEXT.__const: 0x250
-  __TEXT.__cstring: 0x1660b
+  __TEXT.__cstring: 0x1662b
   __TEXT.__oslogstring: 0x28903
   __TEXT.__gcc_except_tab: 0x3ca0
   __TEXT.__dlopen_cstrs: 0x2eb
   __TEXT.__ustring: 0x160
   __TEXT.__unwind_info: 0x7ea4
   __TEXT.__objc_classname: 0x6451
-  __TEXT.__objc_methname: 0x3bb58
-  __TEXT.__objc_methtype: 0x971f
-  __TEXT.__objc_stubs: 0x20240
+  __TEXT.__objc_methname: 0x3bc3c
+  __TEXT.__objc_methtype: 0x976e
+  __TEXT.__objc_stubs: 0x20260
   __DATA_CONST.__got: 0x7a8
   __DATA_CONST.__const: 0x64e0
   __DATA_CONST.__objc_classlist: 0x1098
   __DATA_CONST.__objc_catlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x248
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x396c8
-  __DATA_CONST.__objc_selrefs: 0xb630
+  __DATA_CONST.__objc_const: 0x39778
+  __DATA_CONST.__objc_selrefs: 0xb648
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_classrefs: 0x1430
   __DATA_CONST.__objc_superrefs: 0xfd8

   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__auth_got: 0xc00
   __AUTH.__objc_data: 0xa550
-  __DATA.__objc_ivar: 0x1a84
+  __DATA.__objc_ivar: 0x1a88
   __DATA.__data: 0x1bd0
   __DATA.__bss: 0x360
   __DATA.__common: 0x8

   - /usr/lib/libcupolicy.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 43AB4CD3-D415-39F9-92DE-6D5CCD770FAA
-  Functions: 13045
-  Symbols:   39088
-  CStrings:  16123
+  UUID: 0414B5BA-F255-3CBC-8D8A-EAF758EB73C0
+  Functions: 13049
+  Symbols:   39098
+  CStrings:  16130
 
Symbols:
+ -[NPKPassAssociatedInfo hasDeviceBoundCommutePlans]
+ -[NPKPassAssociatedInfo initWithTransitProperties:appletState:balanceFields:commutePlanFields:tiles:rangingSuspensionReason:hasDeviceBoundCommutePlans:]
+ -[NPKPassesManager group:didInsertAssociatedAccount:forPass:]
+ -[NPKPassesManager group:didRemoveAssociatedAccountForPass:]
+ -[NPKPassesManager group:didUpdateAssociatedAccount:forPass:]
+ GCC_except_table38
+ _OBJC_IVAR_$_NPKPassAssociatedInfo._hasDeviceBoundCommutePlans
+ _objc_msgSend$hasDeviceBoundCommutePlans
+ _objc_msgSend$initWithTransitProperties:appletState:balanceFields:commutePlanFields:tiles:rangingSuspensionReason:hasDeviceBoundCommutePlans:
- -[NPKPassAssociatedInfo initWithTransitProperties:appletState:balanceFields:commutePlanFields:tiles:rangingSuspensionReason:]
- GCC_except_table35
- _objc_msgSend$initWithTransitProperties:appletState:balanceFields:commutePlanFields:tiles:rangingSuspensionReason:
CStrings:
+ "<%@:%p> {transitProperties:%@, appletState:%@, balanceFields:%@ commutePlanFields:%@, tiles:%@, rangingSuspensionReason:%lu, hasDeviceBoundCommutePlans:%lu"
+ "@68@0:8@16@24@32@40@48Q56B64"
+ "TB,R,N,V_hasDeviceBoundCommutePlans"
+ "_hasDeviceBoundCommutePlans"
+ "group:didInsertAssociatedAccount:forPass:"
+ "group:didRemoveAssociatedAccountForPass:"
+ "group:didUpdateAssociatedAccount:forPass:"
+ "initWithTransitProperties:appletState:balanceFields:commutePlanFields:tiles:rangingSuspensionReason:hasDeviceBoundCommutePlans:"
+ "v32@0:8@\"PKGroup\"16@\"PKPass\"24"
+ "v40@0:8@\"PKGroup\"16@\"PKAccount\"24@\"PKPass\"32"
- "<%@:%p> {transitProperties:%@, appletState:%@, balanceFields:%@ commutePlanFields:%@, tiles:%@, rangingSuspensionReason:%lu"
- "@64@0:8@16@24@32@40@48Q56"
- "initWithTransitProperties:appletState:balanceFields:commutePlanFields:tiles:rangingSuspensionReason:"

```
