## MDMClientLibrary

> `/System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary`

```diff

-52.0.0.0.0
-  __TEXT.__text: 0x1f428
-  __TEXT.__auth_stubs: 0x8e0
+54.0.0.0.0
+  __TEXT.__text: 0x1f42c
+  __TEXT.__auth_stubs: 0x8d0
   __TEXT.__objc_methlist: 0x1da4
   __TEXT.__const: 0xd1
   __TEXT.__gcc_except_tab: 0x520
   __TEXT.__cstring: 0x2420
-  __TEXT.__oslogstring: 0x2f1c
+  __TEXT.__oslogstring: 0x2f1d
   __TEXT.__dlopen_cstrs: 0xb7
   __TEXT.__unwind_info: 0x838
   __TEXT.__objc_classname: 0x336
   __TEXT.__objc_methname: 0x556f
   __TEXT.__objc_methtype: 0xbc9
   __TEXT.__objc_stubs: 0x3920
-  __DATA_CONST.__got: 0x3a8
+  __DATA_CONST.__got: 0x3b0
   __DATA_CONST.__const: 0x11b0
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x70

   __DATA_CONST.__objc_selrefs: 0x13a8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x78
-  __AUTH_CONST.__auth_got: 0x480
+  __AUTH_CONST.__auth_got: 0x478
   __AUTH_CONST.__const: 0x3c0
   __AUTH_CONST.__cfstring: 0x3300
   __AUTH_CONST.__objc_const: 0x3a10

   - /System/Library/PrivateFrameworks/DEPClientLibrary.framework/DEPClientLibrary
   - /System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9E74DAE2-1CF1-38EB-8340-A963B8BCA878
+  UUID: A0679FA6-18B9-3D63-9BA0-FAC4602FD91C
   Functions: 681
   Symbols:   2935
   CStrings:  1982
Symbols:
+ _OBJC_CLASS_$_UMUserManager
- _DMCUMUserManagerClass
Functions:
~ +[MDMCheckInRequest _userFieldsForRequest] : 284 -> 288
CStrings:
+ "MDMProvisioningProfileTrust AMFI successfully untrusted provisioning profile: %{public}@"
- "MDMProvisioningProfileTrust AMFI succesfully untrusted provisioning profile: %{public}@"

```
