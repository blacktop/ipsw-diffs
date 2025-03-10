## nfcd

> `/usr/libexec/nfcd`

```diff

-354.25.0.0.0
-  __TEXT.__text: 0x2777c4
+354.26.0.0.0
+  __TEXT.__text: 0x2791b4
   __TEXT.__auth_stubs: 0x17e0
   __TEXT.__delay_helper: 0xec
-  __TEXT.__objc_stubs: 0xd980
-  __TEXT.__objc_methlist: 0x98e0
+  __TEXT.__objc_stubs: 0xd9c0
+  __TEXT.__objc_methlist: 0x98f8
   __TEXT.__const: 0x12e0
   __TEXT.__dlopen_cstrs: 0x5a1
-  __TEXT.__oslogstring: 0x24df4
-  __TEXT.__cstring: 0x2f20e
+  __TEXT.__oslogstring: 0x2509a
+  __TEXT.__cstring: 0x2f5e3
   __TEXT.__objc_classname: 0x1bd9
-  __TEXT.__objc_methname: 0x175ca
-  __TEXT.__objc_methtype: 0x547a
-  __TEXT.__gcc_except_tab: 0x7f2c
-  __TEXT.__unwind_info: 0x3920
+  __TEXT.__objc_methname: 0x17663
+  __TEXT.__objc_methtype: 0x548a
+  __TEXT.__gcc_except_tab: 0x7fd8
+  __TEXT.__unwind_info: 0x3948
   __DATA_CONST.__auth_got: 0xc00
   __DATA_CONST.__got: 0x448
-  __DATA_CONST.__const: 0x7590
-  __DATA_CONST.__cfstring: 0x10b40
+  __DATA_CONST.__const: 0x75a8
+  __DATA_CONST.__cfstring: 0x10ba0
   __DATA_CONST.__objc_classlist: 0x5d0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x378
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x1c8
   __DATA_CONST.__objc_superrefs: 0x420
-  __DATA_CONST.__objc_intobj: 0x6f18
+  __DATA_CONST.__objc_intobj: 0x6f30
   __DATA_CONST.__objc_arraydata: 0x1cf8
   __DATA_CONST.__objc_arrayobj: 0x2b8
   __DATA_CONST.__objc_dictobj: 0xe88
   __DATA.__objc_const: 0x13970
-  __DATA.__objc_selrefs: 0x5508
+  __DATA.__objc_selrefs: 0x5528
   __DATA.__objc_ivar: 0xfdc
   __DATA.__objc_data: 0x3a20
   __DATA.__data: 0x2a48

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4481
+  Functions: 4487
   Symbols:   529
-  CStrings:  12372
+  CStrings:  12403
 
CStrings:
+ "%c[%{public}s %{public}s]:%i (%{public}@) state=%lu"
+ "%c[%{public}s %{public}s]:%i (type=%lu) isFirstAssert=%d, currentVal=%ld, updatedVal=%ld"
+ "%c[%{public}s %{public}s]:%i (type=%lu) lastAssertion=%d, updatedVal=%ld"
+ "%c[%{public}s %{public}s]:%i Assertion [%{public}@, state=%lu] already de-asserted"
+ "%c[%{public}s %{public}s]:%i Assertion [%{public}@, state=%lu] released from PID %d (%{public}@)"
+ "%c[%{public}s %{public}s]:%i Checking HW state again - retries = %lu"
+ "%c[%{public}s %{public}s]:%i HW State is now valid"
+ "%c[%{public}s %{public}s]:%i max tries reached waiting for valid hw sate"
+ "%s assertion mismatched! (Asserter count=%ld, walletPresentationServiceAssertion count=%ld"
+ "-[_NFHardwareManager(Assertion) _requestAssertion:xpcConnection:waitOnComplete:completion:]_block_invoke"
+ "Assertion integrity failure"
+ "B40@0:8Q16^B24^q32"
+ "NFAsserter out-of-sync"
+ "NFAssertionPKPassForegroundPresentment"
+ "NFAssertionSuppressDefaultAppPresentment"
+ "NFAssertionSuppressFieldDetectDefaultAppPresentment"
+ "NFCD built from (B&I) Stockholm_Base-354.26"
+ "_NFHardwareManager+Assertion.m"
+ "assert:isFirst:updatedVal:"
+ "assert:updatedVal:"
+ "currentAssertionCounts:"
+ "deassert:isLast:updatedVal:"
+ "deassert:updatedVal:"
+ "internalAsserter.state == NFAsserterStateIdle"
+ "isAsserted:currentCount:"
+ "obj count=%lu, ref count=%ld"
+ "selectISD"
+ "v24@0:8^q16"
+ "waitForHWSupportedOnConnection:maxTries:callback:"
- "B32@0:8Q16^B24"
- "NFCD built from (B&I) Stockholm_Base-354.25"
- "assert:"
- "assert:isFirst:"
- "deassert:"
- "deassert:isLast:"

```
