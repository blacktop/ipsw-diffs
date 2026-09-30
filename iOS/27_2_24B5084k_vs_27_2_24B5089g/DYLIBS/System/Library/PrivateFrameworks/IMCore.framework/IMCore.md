## IMCore

> `/System/Library/PrivateFrameworks/IMCore.framework/IMCore`

```diff

-1491.200.63.2.1
-  __TEXT.__text: 0x2eda9c
+1491.200.73.0.0
+  __TEXT.__text: 0x2ee2c0
   __TEXT.__delay_stubs: 0x80
   __TEXT.__delay_helper: 0x14c
   __TEXT.__objc_methlist: 0x1906c
   __TEXT.__const: 0x116f0
-  __TEXT.__gcc_except_tab: 0x11928
+  __TEXT.__gcc_except_tab: 0x1196c
   __TEXT.__cstring: 0x13175
-  __TEXT.__oslogstring: 0x23dbb
+  __TEXT.__oslogstring: 0x2409b
   __TEXT.__ustring: 0xc0
   __TEXT.__dlopen_cstrs: 0x184
   __TEXT.__swift5_typeref: 0x39ae

   __TEXT.__swift_as_ret: 0x130
   __TEXT.__swift_as_cont: 0x2e0
   __TEXT.__swift5_mpenum: 0x40
-  __TEXT.__unwind_info: 0xe688
-  __TEXT.__eh_frame: 0x72c8
+  __TEXT.__unwind_info: 0xe6a8
+  __TEXT.__eh_frame: 0x72f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__auth_got: 0x2228
-  __AUTH.__objc_data: 0x4110
-  __AUTH.__data: 0x2d20
+  __AUTH.__objc_data: 0x4700
+  __AUTH.__data: 0x2e40
   __DATA.__objc_ivar: 0x12f8
-  __DATA.__data: 0x65b8
+  __DATA.__data: 0x65e0
   __DATA.__common: 0x7f8
-  __DATA_DIRTY.__objc_data: 0x1e38
-  __DATA_DIRTY.__data: 0x3f8
-  __DATA_DIRTY.__bss: 0x348
+  __DATA_DIRTY.__objc_data: 0x1848
+  __DATA_DIRTY.__data: 0x298
+  __DATA_DIRTY.__bss: 0x310
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 15190
+  Functions: 15196
   Symbols:   2726
-  CStrings:  5014
+  CStrings:  5024
 
CStrings:
+ "Attempting to update display name for chat GUID: %@"
+ "Chat %p is not registered under any GUID; attempting to send display name update to %@ rather than dropping it"
+ "Ignoring group identity update for chat guid: %@"
+ "Skipping display name update: chat style %ld does not allow rename (not business/Stewie/RCS) name=%@"
+ "Skipping display name update: current chat has no name and the incoming name is empty/whitespace."
+ "Skipping display name update: string-equal to current name %@"
+ "Skipping display name update: unchanged (name=%@ style=%ld)"
+ "Suppressing group-title breadcrumb (coalesced): title=%@ prevTitle=%@ sender=%@"
+ "We found fallback chat guids: %@"
+ "We have attempted to re-find the current chat but were unable to. Failed to set display name."
```
