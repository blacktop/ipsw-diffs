## ConfigurationProfilesUI

> `/System/Library/PrivateFrameworks/ConfigurationProfilesUI.framework/Versions/A/ConfigurationProfilesUI`

```diff

-1911.1.1.0.0
-  __TEXT.__text: 0x58e30
-  __TEXT.__objc_methlist: 0x31a8
+1911.40.8.0.0
+  __TEXT.__text: 0x59548
+  __TEXT.__objc_methlist: 0x31b8
   __TEXT.__const: 0xa0
-  __TEXT.__gcc_except_tab: 0xb9b0
-  __TEXT.__cstring: 0xe088
+  __TEXT.__gcc_except_tab: 0xbaac
+  __TEXT.__cstring: 0xe279
   __TEXT.__ustring: 0x60
   __TEXT.__dlopen_cstrs: 0x129
   __TEXT.__oslogstring: 0xe
-  __TEXT.__unwind_info: 0x2b08
+  __TEXT.__unwind_info: 0x2b40
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2aa8
+  __DATA_CONST.__objc_selrefs: 0x2ab0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x318
   __DATA_CONST.__got: 0x7f0
-  __AUTH_CONST.__const: 0x1bc0
-  __AUTH_CONST.__cfstring: 0xb6e0
-  __AUTH_CONST.__objc_const: 0x4c38
+  __AUTH_CONST.__const: 0x1c20
+  __AUTH_CONST.__cfstring: 0xb780
+  __AUTH_CONST.__objc_const: 0x4c40
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x1e0

   - /usr/lib/libbootpolicy.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1756
-  Symbols:   4226
-  CStrings:  1625
+  Functions: 1761
+  Symbols:   4235
+  CStrings:  1631
 
Symbols:
+ __78-[AccountEnrollmentController requestDevicePasscodeDataWithCompletionHandler:]_block_invoke
+ __Z26CurrentUserIsAdministratorv
+ __Z49StartPromptForInstallMDMAuthWithPersonaCredentialP8NSWindowU13block_pointerFvbP12NSDictionaryP6NSDataE
+ ____Z49StartPromptForInstallMDMAuthWithPersonaCredentialP8NSWindowU13block_pointerFvbP12NSDictionaryP6NSDataE_block_invoke
+ ____Z49StartPromptForInstallMDMAuthWithPersonaCredentialP8NSWindowU13block_pointerFvbP12NSDictionaryP6NSDataE_block_invoke_2
+ ___block_descriptor_48_ea8_32bs_e25_v20?0B8"NSDictionary"12l
+ ___block_descriptor_48_ea8_32s40bs_e36_v28?0B8"NSDictionary"12"NSData"20l
+ _mbr_check_membership_by_id
+ _mbr_uid_to_uuid
CStrings:
+ "Console user is not an administrator - prompting for admin install rights and the console user's own credential separately"
+ "Prompting console user for their own credential completed.  Acquired: %@  ExtAuth: <%@>"
+ "Prompting for admin MDM install rights completed.  Acquired: %@  ExtAuth: <%@>"
+ "Unable to check admin group membership for uid %@: %@.  Assuming user is not an administrator."
+ "Unable to get uuid for uid %@: %@.  Assuming user is not an administrator."
+ "v28@?0B8@\"NSDictionary\"12@\"NSData\"20"
```
