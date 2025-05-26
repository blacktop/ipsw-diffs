## GSS

> `/System/Library/Frameworks/GSS.framework/GSS`

```diff

-689.0.0.0.0
-  __TEXT.__text: 0x27d20
-  __TEXT.__auth_stubs: 0x1ed0
-  __TEXT.__const: 0x412
-  __TEXT.__cstring: 0x3b9b
+689.140.1.0.0
+  __TEXT.__text: 0x28244
+  __TEXT.__auth_stubs: 0x1ef0
+  __TEXT.__const: 0x422
+  __TEXT.__cstring: 0x3b55
   __TEXT.__oslogstring: 0xb
-  __TEXT.__unwind_info: 0x718
-  __DATA_CONST.__got: 0x158
+  __TEXT.__unwind_info: 0x71c
+  __DATA_CONST.__got: 0x180
   __DATA_CONST.__const: 0x1378
   __AUTH_CONST.__cfstring: 0x8a0
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0xf68
+  __AUTH_CONST.__auth_got: 0xf78
   __DATA.__data: 0xd10
   __DATA.__bss: 0x28c
   __DATA.__common: 0x94

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libheimdal-asn1.dylib
   - /usr/lib/libresolv.9.dylib
-  Functions: 642
-  Symbols:   2072
-  CStrings:  674
+  Functions: 643
+  Symbols:   2081
+  CStrings:  673
 
Symbols:
+ _CFDataCreateWithBytesNoCopy
+ _HeimCredDeleteQuery
+ __gss_ntlm_cred_label_get.cold.1
+ _kCFAllocatorNull
+ _kCFNull
+ _kHEIMAttrLabelValue
+ _kHEIMAttrParentCredential
+ _kHEIMAttrServerName
CStrings:
+ "Failed to create dictionary:query != NULL"
- "_gss_ntlm_cred_label_get (GSSCred) -  GSS_S_UNAVAILABLE"
- "_gss_ntlm_cred_label_set (GSSCred) -  GSS_S_UNAVAILABLE"

```
