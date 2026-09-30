## DMCUtilities

> `/System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities`

```diff

-20.4.13.0.0
-  __TEXT.__text: 0x31208
-  __TEXT.__auth_stubs: 0xe50
-  __TEXT.__objc_methlist: 0x29dc
+20.4.16.0.0
+  __TEXT.__text: 0x31534
+  __TEXT.__auth_stubs: 0xe60
+  __TEXT.__objc_methlist: 0x2a0c
   __TEXT.__const: 0x148
   __TEXT.__gcc_except_tab: 0x734
   __TEXT.__cstring: 0x335d
-  __TEXT.__oslogstring: 0x4a95
+  __TEXT.__oslogstring: 0x4afc
   __TEXT.__dlopen_cstrs: 0x165
-  __TEXT.__unwind_info: 0xd38
-  __TEXT.__objc_classname: 0x44d
-  __TEXT.__objc_methname: 0x8ead
-  __TEXT.__objc_methtype: 0x128f
-  __TEXT.__objc_stubs: 0x5980
-  __DATA_CONST.__got: 0x610
+  __TEXT.__unwind_info: 0xd40
+  __TEXT.__objc_classname: 0x450
+  __TEXT.__objc_methname: 0x8f61
+  __TEXT.__objc_methtype: 0x12c5
+  __TEXT.__objc_stubs: 0x59e0
+  __DATA_CONST.__got: 0x658
   __DATA_CONST.__const: 0x1088
   __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2250
+  __DATA_CONST.__objc_selrefs: 0x2270
   __DATA_CONST.__objc_superrefs: 0xa8
-  __AUTH_CONST.__auth_got: 0x738
+  __AUTH_CONST.__auth_got: 0x740
   __AUTH_CONST.__const: 0xcc0
   __AUTH_CONST.__cfstring: 0x3b80
-  __AUTH_CONST.__objc_const: 0x3d30
-  __AUTH_CONST.__objc_intobj: 0x168
+  __AUTH_CONST.__objc_const: 0x3d60
+  __AUTH_CONST.__objc_intobj: 0x180
   __AUTH.__objc_data: 0xd70
-  __DATA.__objc_ivar: 0x1cc
+  __DATA.__objc_ivar: 0x1d0
   __DATA.__data: 0x2b1
   __DATA.__bss: 0x950
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
+  - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1294
-  Symbols:   1965
-  CStrings:  2520
+  Functions: 1298
+  Symbols:   1979
+  CStrings:  2533
 
Symbols:
+ _MISValidateSignature
+ _NSFileProtectionComplete
+ _NSFileProtectionCompleteUnlessOpen
+ _NSFileProtectionCompleteUntilFirstUserAuthentication
+ _NSFileProtectionCompleteWhenUserInactive
+ _NSFileProtectionNone
+ _kCFBooleanFalse
+ _kMISValidationOptionRespectUppTrustAndAuthorization
+ _kMISValidationOptionUnauthoritativeLaunch
+ _kMISValidationOptionValidateSignatureOnly
CStrings:
+ "\x03\x14"
+ "@32@0:8^{__SecCode=}16@24"
+ "@40@0:8@16@24Q32"
+ "B32@0:8^{__SecCode=}16@24"
+ "B40@0:8@16Q24^@32"
+ "DMCAtomicWriteToPath:writeOptions:error:"
+ "DMCAtomicWriteToURL:writeOptions:error:"
+ "DMCWriteToBinaryFile:protectionType:"
+ "Failed to validate path via MISValidateSignature error: %@"
+ "Need to validate path using MIS: %{public}@"
+ "Q24@0:8@16"
+ "TQ,R,N,V_options"
+ "_checkValidityOfStaticCode:path:"
+ "_options"
+ "_signingInfoForStaticCode:path:"
+ "_writingOptionsFromProtectionType:"
+ "initWithDictionary:path:writeOptions:"
+ "options"
- "@24@0:8^{__SecCode=}16"
- "B24@0:8^{__SecCode=}16"
- "DMCAtomicWriteToPath:error:"
- "DMCAtomicWriteToURL:error:"
- "_checkValidityOfStaticCode:"
- "_signingInfoForStaticCode:"

```
