## AMSAccountNotificationPlugin

> `/System/Library/Accounts/Notification/AMSAccountNotificationPlugin.bundle/AMSAccountNotificationPlugin`

```diff

-8.2.30.0.0
-  __TEXT.__text: 0xe454
+8.4.17.0.0
+  __TEXT.__text: 0xdab8
   __TEXT.__auth_stubs: 0x7b0
-  __TEXT.__objc_methlist: 0x4a4
+  __TEXT.__objc_methlist: 0x58c
   __TEXT.__const: 0x14e
-  __TEXT.__cstring: 0xa1d
+  __TEXT.__cstring: 0x9fd
   __TEXT.__gcc_except_tab: 0xec
-  __TEXT.__oslogstring: 0x2662
+  __TEXT.__oslogstring: 0x25ed
   __TEXT.__dlopen_cstrs: 0x1a6
   __TEXT.__constg_swiftt: 0x60
-  __TEXT.__swift5_typeref: 0x9e
+  __TEXT.__swift5_typeref: 0xae
   __TEXT.__swift5_fieldmd: 0x20
   __TEXT.__swift5_capture: 0x28
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x330
+  __TEXT.__swift_as_entry: 0x1c
+  __TEXT.__swift_as_ret: 0x20
+  __TEXT.__unwind_info: 0x328
   __TEXT.__eh_frame: 0x2a8
-  __TEXT.__objc_classname: 0x93
-  __TEXT.__objc_methname: 0x1ede
-  __TEXT.__objc_methtype: 0x306
-  __TEXT.__objc_stubs: 0x1f40
-  __DATA_CONST.__got: 0x1a0
-  __DATA_CONST.__const: 0x4f8
-  __DATA_CONST.__objc_classlist: 0x28
+  __TEXT.__objc_classname: 0x5f
+  __TEXT.__objc_methname: 0x1e33
+  __TEXT.__objc_methtype: 0x2f6
+  __TEXT.__objc_stubs: 0x1ec0
+  __DATA_CONST.__got: 0x190
+  __DATA_CONST.__const: 0x4a0
+  __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x860
-  __DATA_CONST.__objc_superrefs: 0x20
+  __DATA_CONST.__objc_selrefs: 0x8e8
+  __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x28
   __AUTH_CONST.__auth_got: 0x3e8
   __AUTH_CONST.__auth_ptr: 0x20
-  __AUTH_CONST.__const: 0x168
+  __AUTH_CONST.__const: 0x1b8
   __AUTH_CONST.__cfstring: 0x7a0
-  __AUTH_CONST.__objc_const: 0x9a8
+  __AUTH_CONST.__objc_const: 0x520
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x1a0
+  __AUTH.__objc_data: 0x100
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x1c
-  __DATA.__data: 0x130
+  __DATA.__objc_ivar: 0x10
+  __DATA.__data: 0x138
   __DATA.__bss: 0x70
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 197
-  Symbols:   201
-  CStrings:  574
+  Functions: 189
+  Symbols:   197
+  CStrings:  558
 
Symbols:
- _OBJC_CLASS_$_AMSSyncAccountFlagsResult
- _OBJC_METACLASS_$_AMSSyncAccountFlagsResult
- _OBJC_METACLASS_$_AMSSyncAccountFlagsTask
- ___NSDictionary0__struct
CStrings:
+ "%{public}@: [%{public}@] Posting a com.apple.AppleMediaServices.activeicloudaccountchanged notification."
+ "_postActiveiCloudAccountChangedNotification"
+ "com.apple.AppleMediaServices.activeicloudaccountchanged"
- "\x01"
- "%{public}@: [%{public}@] Successfully synced the account flags."
- "%{public}@: [%{public}@] Syncing account flags. account = %{public}@ | flags = %{public}@"
- "%{public}@: [%{public}@] The server provided updated account flags."
- "@\"AMSSyncAccountFlagsResult\"16@?0^@8"
- "@\"NSDictionary\""
- "AMSSyncAccountFlagsResult"
- "AMSSyncAccountFlagsTask"
- "T@\"ACAccount\",&,N,V_account"
- "T@\"NSDictionary\",&,N,V_accountFlags"
- "We can't sync flags from the local account."
- "_accountFlags"
- "ams_setAccountFlags:"
- "initWithAccountFlags:"
- "isEqualToDictionary:"
- "performTaskWithBlock:"
- "setAccountFlags:"
- "sharedAccountsConfig"

```
