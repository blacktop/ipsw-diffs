## CFNetwork

> `/System/Library/Frameworks/CFNetwork.framework/CFNetwork`

```diff

-1568.100.1.0.0
-  __TEXT.__text: 0x26e488
+1568.200.1.0.0
+  __TEXT.__text: 0x26e848
   __TEXT.__auth_stubs: 0x5550
   __TEXT.__delay_stubs: 0x7e8
   __TEXT.__delay_helper: 0x1728
   __TEXT.__objc_methlist: 0x8de8
   __TEXT.__const: 0xc9b6c
-  __TEXT.__gcc_except_tab: 0x14e58
-  __TEXT.__cstring: 0x18d40
-  __TEXT.__oslogstring: 0xf722
+  __TEXT.__gcc_except_tab: 0x14ecc
+  __TEXT.__cstring: 0x18d45
+  __TEXT.__oslogstring: 0xf7ab
   __TEXT.__dof_CFNetwork: 0xf3b
   __TEXT.__unwind_info: 0xbfa0
   __TEXT.__objc_classname: 0x1514
-  __TEXT.__objc_methname: 0x1790b
+  __TEXT.__objc_methname: 0x17917
   __TEXT.__objc_methtype: 0x6c8c
-  __TEXT.__objc_stubs: 0xe600
+  __TEXT.__objc_stubs: 0xe620
   __DATA_CONST.__got: 0xc28
-  __DATA_CONST.__const: 0x9380
+  __DATA_CONST.__const: 0x9378
   __DATA_CONST.__objc_classlist: 0x4d8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4b20
+  __DATA_CONST.__objc_selrefs: 0x4b28
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x3e0
   __DATA_CONST.__objc_arraydata: 0x68
   __AUTH_CONST.__auth_got: 0x2c30
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x13750
-  __AUTH_CONST.__cfstring: 0xf280
+  __AUTH_CONST.__cfstring: 0xf2a0
   __AUTH_CONST.__objc_const: 0x155b0
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x50

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 12843
-  Symbols:   14996
-  CStrings:  9368
+  Functions: 12841
+  Symbols:   14994
+  CStrings:  9374
 
Symbols:
+ _SecPolicySetATSPinning
+ _SecPolicySetSSLHostname
- _SecTrustSetPolicies
- _SecPolicyCreateSSLWithATSPinning
CStrings:
+ "SecTrustCopyPolicies failed %!d(MISSING)"
+ "ResumableUploadState: not allowing HTTP resumeURL to downgrade from HTTPS"
+ "file"
+ "absoluteURL"
+ "SecPolicySetATSPinning failed"
+ "SecTrust has an unexpected number of policies %!l(MISSING)u"
+ "SecPolicySetSSLHostname failed"
- "Connection %!l(MISSING)lu: failed to set policy on deserialized cloned trust %!s(MISSING) [%!l(MISSING)d:%!d(MISSING)]"

```
