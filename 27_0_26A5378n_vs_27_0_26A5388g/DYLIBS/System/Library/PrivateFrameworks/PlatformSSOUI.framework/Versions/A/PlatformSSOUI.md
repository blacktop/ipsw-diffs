## PlatformSSOUI

> `/System/Library/PrivateFrameworks/PlatformSSOUI.framework/Versions/A/PlatformSSOUI`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA.__data`

```diff

-643.0.21.0.0
-  __TEXT.__text: 0x248fc
-  __TEXT.__objc_methlist: 0x1d8c
+643.0.33.0.0
+  __TEXT.__text: 0x24e24
+  __TEXT.__objc_methlist: 0x1dc4
   __TEXT.__const: 0x184
-  __TEXT.__oslogstring: 0x7f6
+  __TEXT.__oslogstring: 0x876
   __TEXT.__cstring: 0x1274
-  __TEXT.__gcc_except_tab: 0xa84
+  __TEXT.__gcc_except_tab: 0xa9c
   __TEXT.__swift5_typeref: 0x162
   __TEXT.__swift5_capture: 0xd0
   __TEXT.__constg_swiftt: 0x2c

   __TEXT.__swift_as_entry: 0x24
   __TEXT.__swift_as_ret: 0x20
   __TEXT.__swift_as_cont: 0x18
-  __TEXT.__unwind_info: 0x900
+  __TEXT.__unwind_info: 0x920
   __TEXT.__eh_frame: 0x440
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11c0
+  __DATA_CONST.__objc_selrefs: 0x11f0
   __DATA_CONST.__objc_superrefs: 0x80
-  __DATA_CONST.__got: 0x250
+  __DATA_CONST.__got: 0x258
   __AUTH_CONST.__const: 0x898
   __AUTH_CONST.__cfstring: 0xf80
-  __AUTH_CONST.__objc_const: 0x5d68
+  __AUTH_CONST.__objc_const: 0x5d98
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH_CONST.__auth_got: 0x3e8
+  __AUTH_CONST.__auth_got: 0x410
   __AUTH.__objc_data: 0x5a0
-  __DATA.__objc_ivar: 0x278
+  __DATA.__objc_ivar: 0x27c
   __DATA.__data: 0x520
   __DATA.__bss: 0xf0
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 830
-  Symbols:   1731
-  CStrings:  221
+  Functions: 839
+  Symbols:   1751
+  CStrings:  223
 
Symbols:
+ -[POBuddyUserRegistrationManager cancelConfigStallTimer]
+ -[POBuddyUserRegistrationManager configStallTimer]
+ -[POBuddyUserRegistrationManager dealloc]
+ -[POBuddyUserRegistrationManager setConfigStallTimer:]
+ -[POBuddyUserRegistrationManager startConfigStallTimer]
+ GCC_except_table14
+ GCC_except_table33
+ GCC_except_table41
+ GCC_except_table51
+ GCC_except_table58
+ OBJC_IVAR_$_POBuddyUserRegistrationManager._configStallTimer
+ __55-[POBuddyUserRegistrationManager startConfigStallTimer]_block_invoke
+ ___55-[POBuddyUserRegistrationManager startConfigStallTimer]_block_invoke
+ __dispatch_source_type_timer
+ _dispatch_resume
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
+ _objc_msgSend$cancelConfigStallTimer
+ _objc_msgSend$configStallTimer
+ _objc_msgSend$extensionTeamIdentifier
+ _objc_msgSend$isConfigurationActiveForExtensionIdentifier:teamIdentifier:runningAsAgent:completion:
+ _objc_msgSend$setConfigStallTimer:
+ _objc_msgSend$startConfigStallTimer
- GCC_except_table27
- GCC_except_table37
- GCC_except_table47
- GCC_except_table54
- _objc_msgSend$isConfigurationActiveForExtensionIdentifier:runningAsAgent:completion:
CStrings:
+ "Configuration did not arrive within %d seconds; surfacing retry status pane."
+ "Failed to create config stall watchdog timer"
```
