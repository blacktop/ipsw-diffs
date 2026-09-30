## nfcd

> `/usr/libexec/nfcd`

```diff

-351.10.0.0.0
-  __TEXT.__text: 0x268d4c
-  __TEXT.__auth_stubs: 0x17d0
+352.7.0.0.0
+  __TEXT.__text: 0x269a00
+  __TEXT.__auth_stubs: 0x17c0
   __TEXT.__delay_helper: 0xec
-  __TEXT.__objc_stubs: 0xd820
-  __TEXT.__objc_methlist: 0x7854
+  __TEXT.__objc_stubs: 0xd8a0
+  __TEXT.__objc_methlist: 0x785c
   __TEXT.__const: 0x11c0
-  __TEXT.__oslogstring: 0x23f7a
-  __TEXT.__cstring: 0x2dc0b
+  __TEXT.__oslogstring: 0x240c3
+  __TEXT.__cstring: 0x2de02
   __TEXT.__objc_classname: 0x1bad
-  __TEXT.__objc_methname: 0x16a86
+  __TEXT.__objc_methname: 0x16b1f
   __TEXT.__objc_methtype: 0x5331
-  __TEXT.__gcc_except_tab: 0x7614
-  __TEXT.__dlopen_cstrs: 0x549
-  __TEXT.__unwind_info: 0x3698
-  __DATA_CONST.__auth_got: 0xbf8
-  __DATA_CONST.__got: 0x428
-  __DATA_CONST.__const: 0x7930
-  __DATA_CONST.__cfstring: 0x10140
+  __TEXT.__gcc_except_tab: 0x7674
+  __TEXT.__dlopen_cstrs: 0x5a1
+  __TEXT.__unwind_info: 0x36a8
+  __DATA_CONST.__auth_got: 0xbf0
+  __DATA_CONST.__got: 0x438
+  __DATA_CONST.__const: 0x7948
+  __DATA_CONST.__cfstring: 0x101c0
   __DATA_CONST.__objc_classlist: 0x5b8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x380
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x1c8
   __DATA_CONST.__objc_superrefs: 0x3f0
-  __DATA_CONST.__objc_intobj: 0x6c78
+  __DATA_CONST.__objc_intobj: 0x6c60
   __DATA_CONST.__objc_arraydata: 0x1df0
   __DATA_CONST.__objc_arrayobj: 0x378
   __DATA_CONST.__objc_dictobj: 0xf28
-  __DATA.__objc_const: 0x16c18
-  __DATA.__objc_selrefs: 0x5240
-  __DATA.__objc_ivar: 0xf50
+  __DATA.__objc_const: 0x16c38
+  __DATA.__objc_selrefs: 0x5268
+  __DATA.__objc_ivar: 0xf54
   __DATA.__objc_data: 0x3930
   __DATA.__data: 0x2ab0
-  __DATA.__bss: 0x500
+  __DATA.__bss: 0x518
   __DATA.__common: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4356
-  Symbols:   524
-  CStrings:  12053
+  Functions: 4360
+  Symbols:   525
+  CStrings:  12076
 
Symbols:
+ _OBJC_CLASS_$_LSApplicationExtensionRecord
+ _OBJC_CLASS_$_LSBundleRecord
- _os_eligibility_get_domain_answer
CStrings:
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) %!{(MISSING)public}@ : HW state = %!u(MISSING)"
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) Client is ExtensionKit extension"
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) Client is not supported by CoreNFC"
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) Invalid"
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) Non-bundle process"
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) Notifying client of state update : %!u(MISSING)."
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) Processing %!{(MISSING)public}@ : HW state = %!u(MISSING)"
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) Record error=%!{(MISSING)public}@"
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) Valid CoreNFC client"
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) eligibility framework unavailable"
+ "Class getOSEligibilityQueryClass(void)_block_invoke"
+ "NFCD built from (B&I) Stockholm_Base-352.7"
+ "OSEligibilityQuery"
+ "T@\"NSMutableOrderedSet\",&,N,V_paymentAIDPrefixes"
+ "_didUsePaymentInSession"
+ "_initPaymentAIDPrefixList"
+ "_isValidClient:"
+ "_paymentAIDPrefixes"
+ "answer"
+ "bundleRecordForAuditToken:error:"
+ "connectedDurationDim"
+ "developerType"
+ "didUsePaymentAid"
+ "durationDim"
+ "initWithDomain:auditToken:error:"
+ "initWithURL:requireValid:error:"
+ "paymentAIDPrefixes"
+ "pollingDurationDim"
+ "sessionDurationDim"
+ "setPaymentAIDPrefixes:"
+ "softlink:o:path:/System/Library/PrivateFrameworks/OSEligibility.framework/OSEligibility"
+ "void *OSEligibilityLibrary(void)"
- "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) Error=%!d(MISSING)"
- "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) Notifying client of state update."
- "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) Processing %!{(MISSING)public}@"
- "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) errno=%!{(MISSING)public}d"
- "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) state = %!l(MISSING)u"
- "NFCD built from (B&I) Stockholm_Base-351.10"
- "T@\"NSMutableOrderedSet\",&,N,V_paymentAIDList"
- "_initPaymentAIDList"
- "_isCoreNFC"
- "_paymentAIDList"
- "didUsePaymentAID"
- "getHardwareState"
- "paymentAIDList"
- "setPaymentAIDList:"

```
