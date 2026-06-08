## deferredmediad

> `/usr/libexec/deferredmediad`

```diff

-665.120.8.0.0
-  __TEXT.__text: 0x1ac
-  __TEXT.__auth_stubs: 0xc0
-  __TEXT.__const: 0x24
-  __TEXT.__gcc_except_tab: 0x28
+748.0.0.122.2
+  __TEXT.__text: 0x298
+  __TEXT.__auth_stubs: 0xf0
+  __TEXT.__objc_stubs: 0x80
+  __TEXT.__const: 0x2c
+  __TEXT.__gcc_except_tab: 0x38
   __TEXT.__cstring: 0x1f
-  __TEXT.__unwind_info: 0x68
-  __DATA_CONST.__auth_got: 0x68
-  __DATA_CONST.__got: 0x20
+  __TEXT.__oslogstring: 0x59
+  __TEXT.__objc_methname: 0x5c
+  __TEXT.__unwind_info: 0x70
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x88
+  __DATA_CONST.__got: 0x40
+  __DATA.__objc_selrefs: 0x20
   __DATA.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EA2D7ACA-3719-3346-B483-D1A247DADD27
-  Functions: 2
-  Symbols:   19
-  CStrings:  2
+  UUID: AA2C44CB-7CE1-385A-A3B7-0F398BC2CE9B
+  Functions: 3
+  Symbols:   27
+  CStrings:  7
 
Symbols:
+ _NSTemporaryDirectory
+ _NSURLFileProtectionCompleteUntilFirstUserAuthentication
+ _NSURLFileProtectionKey
+ _OBJC_CLASS_$_NSURL
+ __os_log_default
+ __os_log_error_impl
+ _objc_msgSend
+ _os_log_type_enabled
CStrings:
+ "Error setting NSURLFileProtectionCompleteUntilFirstUserAuthentication for %{public}@: %s"
+ "UTF8String"
+ "fileURLWithPath:isDirectory:"
+ "localizedDescription"
+ "setResourceValue:forKey:error:"

```
