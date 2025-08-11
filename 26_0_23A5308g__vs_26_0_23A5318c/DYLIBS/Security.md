## Security

> `/System/Library/Frameworks/Security.framework/Security`

```diff

-61901.0.84.0.0
-  __TEXT.__text: 0x17ba20
+61901.0.87.0.1
+  __TEXT.__text: 0x17bb20
   __TEXT.__auth_stubs: 0x3fe0
   __TEXT.__objc_methlist: 0x629c
   __TEXT.__const: 0xd728
   __TEXT.__dlopen_cstrs: 0xbc
-  __TEXT.__cstring: 0x18161
+  __TEXT.__cstring: 0x1817b
   __TEXT.__gcc_except_tab: 0x8b54
   __TEXT.__oslogstring: 0xf7ed
   __TEXT.__ustring: 0x406
   __TEXT.__dof_codesign: 0x1ffd
   __TEXT.__dof_security_: 0x325
-  __TEXT.__unwind_info: 0x5fc8
+  __TEXT.__unwind_info: 0x5fc0
   __TEXT.__objc_classname: 0xaf8
   __TEXT.__objc_methname: 0xc057
   __TEXT.__objc_methtype: 0x36f4

   __DATA_CONST.__objc_arraydata: 0x100
   __AUTH_CONST.__auth_got: 0x2008
   __AUTH_CONST.__const: 0x4398
-  __AUTH_CONST.__cfstring: 0x162e0
+  __AUTH_CONST.__cfstring: 0x16300
   __AUTH_CONST.__objc_const: 0x9de8
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_intobj: 0x168

   - /usr/lib/libcoretls_cfhelpers.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 60D78A0D-E77B-3F57-8E30-98837BC173F6
+  UUID: 48FE5C49-984F-3983-9A7B-EDC3F74A9607
   Functions: 6969
   Symbols:   20688
-  CStrings:  11171
+  CStrings:  11173
 
Symbols:
+ ___block_descriptor_tmp.1199
+ ___block_descriptor_tmp.1203
+ ___block_literal_global.1205
+ _apply_block_2.13973
- ___block_descriptor_tmp.1196
- ___block_descriptor_tmp.1200
- ___block_literal_global.1202
- _apply_block_2.13974
Functions:
~ ___SecTrustEvaluateIfNecessaryFastAsync_block_invoke_2.556 : 32 -> 84
~ _X509PolicySetFlagsForCommonNames : 272 -> 276
~ _X509ExtensionParseAppleExtension : 2624 -> 2672
~ _SecPolicyCreateAppleSoftwareSigning : 268 -> 308
~ _SecPolicyCreateMacOSProfileApplicationSigning : 296 -> 336
~ ___SecTrustEvaluateIfNecessaryFastAsync_block_invoke_2.547 : 32 -> 84
~ __ZN8Security11CodeSigning11Requirement11Interpreter4evalEi : 4140 -> 4160
CStrings:
+ "1.2.840.113635.100.6.22.1"

```
