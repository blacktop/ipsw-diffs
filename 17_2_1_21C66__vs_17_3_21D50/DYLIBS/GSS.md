## GSS

> `/System/Library/Frameworks/GSS.framework/GSS`

```diff

-685.0.0.0.0
-  __TEXT.__text: 0x27b20
-  __TEXT.__auth_stubs: 0x1ea0
+687.0.0.0.0
+  __TEXT.__text: 0x27d1c
+  __TEXT.__auth_stubs: 0x1ed0
   __TEXT.__const: 0x412
-  __TEXT.__cstring: 0x3bc8
+  __TEXT.__cstring: 0x3b9b
   __TEXT.__oslogstring: 0xb
   __TEXT.__unwind_info: 0x718
   __DATA_CONST.__got: 0x158
   __DATA_CONST.__const: 0x1378
   __AUTH_CONST.__cfstring: 0x8a0
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0xf50
+  __AUTH_CONST.__auth_got: 0xf68
   __DATA.__data: 0xd10
   __DATA.__bss: 0x28c
   __DATA.__common: 0x94

   - /usr/lib/libheimdal-asn1.dylib
   - /usr/lib/libresolv.9.dylib
   Functions: 642
-  Symbols:   2069
-  CStrings:  675
+  Symbols:   2072
+  CStrings:  674
 
Symbols:
+ _CFStringGetLength
+ _HeimCredReleaseTransient
+ _HeimCredRetainTransient
CStrings:
+ "Failed to create dictionary:baseQuery != NULL"
- "Failed to create dictionary:query != NULL"
- "change_hold (NTLM)(GSSCred) -  GSS_S_UNAVAILABLE"

```
