## AppSSOKerberos

> `/System/Library/PrivateFrameworks/AppSSOKerberos.framework/AppSSOKerberos`

```diff

-483.60.3.0.0
-  __TEXT.__text: 0x228c8
-  __TEXT.__auth_stubs: 0xf00
-  __TEXT.__objc_methlist: 0x1e54
+483.60.4.0.0
+  __TEXT.__text: 0x22d8c
+  __TEXT.__auth_stubs: 0xf50
+  __TEXT.__objc_methlist: 0x1e5c
   __TEXT.__const: 0x160
-  __TEXT.__oslogstring: 0x2814
-  __TEXT.__cstring: 0x19ab
+  __TEXT.__oslogstring: 0x282b
+  __TEXT.__cstring: 0x1aa2
   __TEXT.__gcc_except_tab: 0x9fc
   __TEXT.__dlopen_cstrs: 0x63
-  __TEXT.__unwind_info: 0x8f0
+  __TEXT.__unwind_info: 0x900
   __TEXT.__objc_classname: 0x2af
-  __TEXT.__objc_methname: 0x5775
+  __TEXT.__objc_methname: 0x5795
   __TEXT.__objc_methtype: 0xadc
   __TEXT.__objc_stubs: 0x3540
   __DATA_CONST.__got: 0x3c0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1490
+  __DATA_CONST.__objc_selrefs: 0x1498
   __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_arraydata: 0x70
-  __AUTH_CONST.__auth_got: 0x790
+  __AUTH_CONST.__auth_got: 0x7b8
   __AUTH_CONST.__const: 0x240
-  __AUTH_CONST.__cfstring: 0x1780
+  __AUTH_CONST.__cfstring: 0x1800
   __AUTH_CONST.__objc_const: 0x34a0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x90

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7B284C2C-17CA-3D22-A1CC-F3189F3553C8
-  Functions: 998
-  Symbols:   3436
-  CStrings:  1866
+  UUID: 7FD7027D-B6C2-3DD6-B261-10D95829F588
+  Functions: 1007
+  Symbols:   3462
+  CStrings:  1876
 
Symbols:
+ -[SOKerberosHelper makeCredentialDefaultWithRealm:]
+ -[SOKerberosHelper makeCredentialDefaultWithRealm:].cold.1
+ -[SOKerberosHelper makeCredentialDefaultWithRealm:].cold.2
+ -[SOKerberosHelper makeCredentialDefaultWithRealm:].cold.3
+ -[SOKerberosHelper makeCredentialDefaultWithRealm:].cold.4
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_9
+ ___block_literal_global.70
+ ___chkstk_darwin
+ _krb5_cc_switch
+ _krb5_cccol_cursor_free
+ _krb5_cccol_cursor_new
+ _krb5_cccol_cursor_next
+ _krb5_realm_compare
- ___block_literal_global.53
CStrings:
+ "%{public}@, %{public}@"
+ "krb5_cc_switch failed when setting default kerberos entry."
+ "krb5_cccol_cursor_new failed when setting default kerberos entry."
+ "krb5_init_context failed when setting default kerberos entry."
+ "krb5_parse_name failed when setting default kerberos entry."
+ "makeCredentialDefaultWithRealm:"

```
