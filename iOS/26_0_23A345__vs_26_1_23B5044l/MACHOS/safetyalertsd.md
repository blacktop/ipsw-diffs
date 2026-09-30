## safetyalertsd

> `/usr/libexec/safetyalertsd`

```diff

-64.0.24.0.0
-  __TEXT.__text: 0xd1d40
-  __TEXT.__auth_stubs: 0xfd0
+64.0.25.0.0
+  __TEXT.__text: 0xd27d0
+  __TEXT.__auth_stubs: 0x1000
   __TEXT.__objc_stubs: 0x2d80
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0xa84
-  __TEXT.__const: 0x9bf8
-  __TEXT.__gcc_except_tab: 0xc4f0
-  __TEXT.__cstring: 0x4fc0
-  __TEXT.__oslogstring: 0x340d3
+  __TEXT.__const: 0x9c18
+  __TEXT.__gcc_except_tab: 0xc5ac
+  __TEXT.__cstring: 0x504b
+  __TEXT.__oslogstring: 0x343af
   __TEXT.__objc_classname: 0x1ea
   __TEXT.__objc_methname: 0x366e
   __TEXT.__objc_methtype: 0x1939
   __TEXT.__ustring: 0x18
-  __TEXT.__unwind_info: 0x3ca0
-  __DATA_CONST.__auth_got: 0x7f8
+  __TEXT.__unwind_info: 0x3cd8
+  __DATA_CONST.__auth_got: 0x810
   __DATA_CONST.__got: 0x4d8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x8118
-  __DATA_CONST.__cfstring: 0x5620
+  __DATA_CONST.__cfstring: 0x5700
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__objc_intobj: 0x18
+  __DATA_CONST.__objc_intobj: 0x30
   __DATA.__objc_const: 0x1160
   __DATA.__objc_selrefs: 0xfc8
   __DATA.__objc_ivar: 0x7c

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9B3DECAF-5A78-39F0-8AB4-240FE1832F9E
-  Functions: 3244
-  Symbols:   426
-  CStrings:  4350
+  UUID: EC27D12A-0C9D-30AC-AD52-08D6F65A7CB2
+  Functions: 3249
+  Symbols:   429
+  CStrings:  4374
 
Symbols:
+ _CFStringGetCStringPtr
+ _IOPMAssertionCreateWithProperties
+ _IOPMAssertionRelease
CStrings:
+ "AssertName"
+ "AssertType"
+ "Category"
+ "I"
+ "PreventUserIdleSystemSleep"
+ "SABLEAdvertisePowerAssertion"
+ "TimeoutAction"
+ "TimeoutActionRelease"
+ "TimeoutSeconds"
+ "{\"msg%{public}.0s\":\"#SAPA,\", \"assertionName\":%{public, location:escape_only}s, \"result\":%{public}d, \"fHasAssertion\":%{public}d, \"fTimeoutSec\":%{public}d, \"fAssertionId\":%{public}d, \"fAssertionIdentifier\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#SAPA,\", \"result\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#SAPA,SAPowerAssertion\", \"fTimeoutSec\":%{public}d, \"fAssertionIdentifier\":%{public, location:escape_only}s, \"fHasAssertion\":%{public}d, \"fAssertionId\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#SAPA,acquire\"}"
+ "{\"msg%{public}.0s\":\"#SAPA,invalid assertion name\"}"
+ "{\"msg%{public}.0s\":\"#SAPA,invalid properties\"}"
+ "{\"msg%{public}.0s\":\"#SAPA,reset\", \"result\":%{public}d, \"fAssertionId\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#SAPA,~SAPowerAssertion\"}"
+ "{\"msg%{public}.0s\":\"#aa,isSignatureValidUsingCodebook,codebook nil\"}"
- "{\"msg%{public}.0s\":\"#aa,isSignatureValidUsingCodebook,fCodebook nil\"}"

```
