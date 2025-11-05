## com.apple.WebDriver.HTTPService

> `/System/Library/PrivateFrameworks/WebDriver.framework/Versions/A/XPCServices/com.apple.WebDriver.HTTPService.xpc/Contents/MacOS/com.apple.WebDriver.HTTPService`

```diff

-7620.2.4.11.6
-  __TEXT.__text: 0x888
-  __TEXT.__auth_stubs: 0x1b0
-  __TEXT.__objc_stubs: 0x1a0
-  __TEXT.__const: 0x18
-  __TEXT.__gcc_except_tab: 0x134
-  __TEXT.__oslogstring: 0x1c4
-  __TEXT.__cstring: 0xe8
-  __TEXT.SandboxProfile: 0xb3f
-  __TEXT.__objc_methname: 0xfb
-  __TEXT.__unwind_info: 0x68
-  __DATA_CONST.__auth_got: 0xe8
-  __DATA_CONST.__got: 0x30
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x40
-  __DATA_CONST.__cfstring: 0x80
+7621.1.15.11.10
+  __TEXT.__text: 0xb4
+  __TEXT.__auth_stubs: 0x50
+  __TEXT.__gcc_except_tab: 0x14
+  __TEXT.SandboxProfile: 0xb3e
+  __TEXT.__unwind_info: 0x60
+  __DATA_CONST.__auth_got: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0x68
-  __DATA.__bss: 0x10
-  - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/JavaScriptCore.framework/Versions/A/JavaScriptCore
   - /System/Library/PrivateFrameworks/SafariCore.framework/Versions/A/SafariCore

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1D120CBA-A415-32D1-A6BC-D1428AA69D0D
-  Functions: 2
-  Symbols:   41
-  CStrings:  39
+  UUID: C779B047-92AD-351D-8560-65D1BB467E47
+  Functions: 1
+  Symbols:   9
+  CStrings:  0
 
Symbols:
+ _WDXPCServiceMain
- _OBJC_CLASS_$_NSBundle
- _OBJC_CLASS_$_NSXPCListener
- _OBJC_CLASS_$_WBSSoftLinkingUtilities
- _OBJC_CLASS_$_WDHTTPService
- _WBSEnableSandboxStyleFileQuarantine
- _WDOSLogXPCService
- __NSConcreteGlobalBlock
- __ZN3WTF20initializeMainThreadEv
- ___CFConstantStringClassReference
- ___chkstk_darwin
- ___error
- ___stack_chk_guard
- __dispatch_main_q
- __os_log_error_impl
- __os_log_impl
- __set_user_dir_suffix
- _confstr
- _dispatch_once
- _exit
- _getenv
- _objc_autoreleasePoolPop
- _objc_autoreleasePoolPush
- _objc_msgSend
- _objc_opt_new
- _objc_release
- _objc_retain
- _objc_retainAutorelease
- _objc_retainAutoreleasedReturnValue
- _os_log_type_enabled
- _os_variant_allows_internal_security_policies
- _realpath$DARWIN_EXTSN
- _sandbox_free_error
- _sandbox_init_with_parameters
Functions:
~ _main : 2144 -> 180
CStrings:
- "../../../../"
- "/Applications/Safari.app"
- "/Applications/Xcode.app/Contents/Developer"
- "APPLICATION_DIR"
- "Could not initialize the sandbox, error: %{public}s."
- "Couldn't enable sandbox style file quarantine."
- "Couldn't retrieve private cache directory path: %d."
- "Couldn't retrieve private temporary directory path: %d."
- "DARWIN_USER_CACHE_DIR"
- "DARWIN_USER_TEMP_DIR"
- "DEVELOPER_DIR"
- "Error calling realpath on the home directory."
- "Error calling realpath on the private cache directory path: %d."
- "Error calling realpath on the private temporary directory path: %d."
- "FRAMEWORKS_DIR"
- "HOME"
- "HOME_DIR"
- "Launched."
- "Whitelisting relocatable app bundle located at path: %@"
- "_setQueue:"
- "bundlePath"
- "bundleWithIdentifier:"
- "bundleWithPath:"
- "com.apple.WebDriver"
- "com.apple.WebInspector"
- "developerPath"
- "fileSystemRepresentation"
- "resume"
- "serviceListener"
- "setDelegate:"
- "stringByAppendingString:"
- "stringByDeletingLastPathComponent"
- "stringByStandardizingPath"
- "v8@?0"
- "webDriver_isSafariFamilyBundle"

```
