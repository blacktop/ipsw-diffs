## Message

> `/System/Library/PrivateFrameworks/Message.framework/Message`

```diff

-3826.400.113.0.0
-  __TEXT.__text: 0xb70b18
-  __TEXT.__auth_stubs: 0x7de0
+3826.400.121.2.2
+  __TEXT.__text: 0xb79fec
+  __TEXT.__auth_stubs: 0x7df0
   __TEXT.__objc_methlist: 0x11a84
   __TEXT.__gcc_except_tab: 0x38694
-  __TEXT.__const: 0x4a960
-  __TEXT.__cstring: 0x3015e
-  __TEXT.__oslogstring: 0x23f20
+  __TEXT.__const: 0x4ab10
+  __TEXT.__cstring: 0x3016e
+  __TEXT.__oslogstring: 0x241b0
   __TEXT.__ustring: 0x23ca
-  __TEXT.__swift5_typeref: 0x1228b
-  __TEXT.__swift5_capture: 0x30d04
-  __TEXT.__constg_swiftt: 0xd620
+  __TEXT.__swift5_typeref: 0x122f1
+  __TEXT.__swift5_capture: 0x31360
+  __TEXT.__constg_swiftt: 0xd6ac
   __TEXT.__swift5_builtin: 0xd98
-  __TEXT.__swift5_reflstr: 0xe8a9
-  __TEXT.__swift5_fieldmd: 0x146ac
+  __TEXT.__swift5_reflstr: 0xe929
+  __TEXT.__swift5_fieldmd: 0x14798
   __TEXT.__swift5_assocty: 0x1b10
-  __TEXT.__swift5_proto: 0x2780
-  __TEXT.__swift5_types: 0x176c
+  __TEXT.__swift5_proto: 0x2794
+  __TEXT.__swift5_types: 0x1780
   __TEXT.__swift5_protos: 0x74
   __TEXT.__swift5_mpenum: 0x7e8
-  __TEXT.__unwind_info: 0x238c0
-  __TEXT.__eh_frame: 0x1e5a0
+  __TEXT.__unwind_info: 0x23930
+  __TEXT.__eh_frame: 0x1e560
   __TEXT.__objc_classname: 0x2a4e
   __TEXT.__objc_methname: 0x2e4a9
   __TEXT.__objc_methtype: 0x67c4

   __DATA_CONST.__objc_protorefs: 0x1c0
   __DATA_CONST.__objc_superrefs: 0x680
   __DATA_CONST.__objc_arraydata: 0xf58
-  __AUTH_CONST.__auth_got: 0x3f08
-  __AUTH_CONST.__auth_ptr: 0x3138
-  __AUTH_CONST.__const: 0xa4aa0
+  __AUTH_CONST.__auth_got: 0x3f10
+  __AUTH_CONST.__auth_ptr: 0x3168
+  __AUTH_CONST.__const: 0xa5cf0
   __AUTH_CONST.__cfstring: 0x184a0
-  __AUTH_CONST.__objc_const: 0x26e50
+  __AUTH_CONST.__objc_const: 0x26e70
   __AUTH_CONST.__objc_arrayobj: 0xb88
   __AUTH_CONST.__objc_intobj: 0xa08
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH.__objc_data: 0x5298
-  __AUTH.__data: 0xaf90
+  __AUTH.__data: 0xaf80
   __DATA.__objc_ivar: 0x13a0
-  __DATA.__data: 0xe828
+  __DATA.__data: 0xe910
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x4e118
-  __DATA.__common: 0xf40
+  __DATA.__bss: 0x4e398
+  __DATA.__common: 0xf48
   __DATA_DIRTY.__objc_data: 0x1900
   __DATA_DIRTY.__data: 0x18
   __DATA_DIRTY.__bss: 0x410

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 54764
+  Functions: 54915
   Symbols:   13899
-  CStrings:  17246
+  CStrings:  17255
 
CStrings:
+ "[%.*hhx-%.*X] Account did change."
+ "[%.*hhx-%.*X] Accounts: Credentials did change for different account."
+ "[%.*hhx-%.*X] Already trying to renew credentials. Skipping."
+ "[%.*hhx-%.*X] Credentials did become invalid. Trying to renew."
+ "[%.*hhx-%.*X] Ignoring credentials-did-change notification while renewing."
+ "[%.*hhx-%.*X] Not syncing Notes mailbox path %{sensitive,mask.mailbox}s"
+ "[%.*hhx-%{public}s] Got post-auth capabilities: %{public}s."
+ "[%.*hhx-%{public}s] Got pre-auth capabilities: %{public}s."
+ "[%.*hhx-%{public}s] XOAUTH2 error: status '%{public}s',  schemes '%{public}s',  scope '%{public}s'"
+ "[%.*hhx] Credentials state -> %{public}s"
+ "[%.*hhx] Not resetting backoff timer."
+ "[%.*hhx] [%{sensitive,mask.mailbox}s] Did mark should temporarily grow window of interest. Fetching missing messages, first."
+ "[%.*hhx] [%{sensitive,mask.mailbox}s] Did mark should temporarily grow window of interest. Waiting for FindMissingMessages."
+ "[%{public}s] Account did change."
+ "isRenewing"
- "[%.*hhx-%.*X] Account changed."
- "[%.*hhx-%.*X] Credentials did become invalid. Trying to renew. (avoid UI: %{BOOL}d)"
- "[%.*hhx-%{public}s] Got post-auth capabilities: %s."
- "[%.*hhx-%{public}s] Got pre-auth capabilities: %s."
- "[%.*hhx-%{public}s] XOAUTH2 error: status '%{public}s',  schemes '%{public}s',  scope '%{private}s'"
- "[%{public}s] Account changed."

```
