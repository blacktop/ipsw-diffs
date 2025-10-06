## AudioDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AudioDiagnosticExtension.appex/AudioDiagnosticExtension`

```diff

-70.2.5.0.0
-  __TEXT.__text: 0x3584
+70.3.1.0.0
+  __TEXT.__text: 0x3a90
   __TEXT.__auth_stubs: 0x2f0
-  __TEXT.__objc_stubs: 0x880
-  __TEXT.__objc_methlist: 0xec
-  __TEXT.__gcc_except_tab: 0x630
+  __TEXT.__objc_stubs: 0x8e0
+  __TEXT.__objc_methlist: 0x104
+  __TEXT.__gcc_except_tab: 0x6c0
   __TEXT.__const: 0x10
-  __TEXT.__cstring: 0x36d
-  __TEXT.__oslogstring: 0x45e
+  __TEXT.__cstring: 0x3eb
+  __TEXT.__oslogstring: 0x53c
   __TEXT.__objc_classname: 0x22
-  __TEXT.__objc_methname: 0x6ff
+  __TEXT.__objc_methname: 0x7a5
   __TEXT.__objc_methtype: 0x9c
-  __TEXT.__unwind_info: 0x10c
+  __TEXT.__unwind_info: 0x110
   __DATA_CONST.__auth_got: 0x188
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__const: 0x40
-  __DATA_CONST.__cfstring: 0x2c0
+  __DATA_CONST.__cfstring: 0x300
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x190
-  __DATA.__objc_selrefs: 0x248
+  __DATA.__objc_const: 0x1c0
+  __DATA.__objc_selrefs: 0x268
   __DATA.__objc_classrefs: 0x78
   __DATA.__objc_superrefs: 0x8
-  __DATA.__objc_ivar: 0x8
+  __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0xa0
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DB56FBFA-7364-37D4-989E-8C2293663184
-  Functions: 20
+  UUID: 3D191CF9-2722-3CC5-8698-39FFB48B643E
+  Functions: 22
   Symbols:   81
-  CStrings:  163
+  CStrings:  175
 
Symbols:
+ _objc_retain_x23
+ _objc_retain_x28
- _objc_retain_x25
- _objc_retain_x27
CStrings:
+ "\x12"
+ "%25s:%-5d Cannot write to directory, falling back to secondary directory. { directory=%{public}@, secondary=%{public}@ }"
+ "%25s:%-5d Failed to create secondary directory. { error=%{public}@ }"
+ "%25s:%-5d Failed to remove file. { path=%{public}@, error=%{public}@ }"
+ "%25s:%-5d Failed to remove item. { path=%{public}@, error=%{public}@"
+ "%25s:%-5d User consent provided: %d"
+ "/private/var/mobile/tmp/AudioCapture/DiagnosticExtensionFiles"
+ "/var/mobile/Library/Logs/CrashReporter/AudioDiagnosticExtension"
+ "T@\"NSString\",&,N,V_validCaptureFilesPath"
+ "_validCaptureFilesPath"
+ "arrayByAddingObjectsFromArray:"
+ "isWritableFileAtPath:"
+ "setValidCaptureFilesPath:"
+ "validCaptureFilesPath"
- "\x11"
- "%25s:%-5d failed to create directory %s. error: %s"
- "%25s:%-5d failed to remove item: %{public}@"
- "%25s:%-5d failed to removeItem error: %{public}s"

```
