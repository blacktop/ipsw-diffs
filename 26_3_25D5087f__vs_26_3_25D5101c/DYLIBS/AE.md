## AE

> `/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/AE.framework/Versions/A/AE`

```diff

-982.2.1.0.0
-  __TEXT.__text: 0x63fb0
-  __TEXT.__auth_stubs: 0x1cd0
-  __TEXT.__const: 0x98c
-  __TEXT.__cstring: 0x33fe
-  __TEXT.__oslogstring: 0x8f02
-  __TEXT.__dof_AE_DTRACE: 0x624
+982.3.2.0.0
+  __TEXT.__text: 0x641e4
+  __TEXT.__auth_stubs: 0x1ce0
+  __TEXT.__const: 0x99c
+  __TEXT.__cstring: 0x33a2
+  __TEXT.__oslogstring: 0x9139
+  __TEXT.__dof_AE_DTRACE: 0x643
   __TEXT.__unwind_info: 0xa0
   __TEXT.__eh_frame: 0x50
-  __DATA_CONST.__got: 0x308
+  __DATA_CONST.__got: 0x318
   __DATA_CONST.__const: 0xaa0
-  __AUTH_CONST.__auth_got: 0xe68
+  __AUTH_CONST.__auth_got: 0xe70
   __AUTH_CONST.__const: 0x17a8
   __AUTH_CONST.__cfstring: 0xc00
   __AUTH.__data: 0x60
   __DATA.__data: 0xc0
-  __DATA.__bss: 0x250
+  __DATA.__bss: 0x258
   __DATA.__common: 0x3
   __DATA_DIRTY.__data: 0xd0
   __DATA_DIRTY.__bss: 0x328

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 1A4F6A04-39DF-3429-9F8F-C1B8420435F7
-  Functions: 1307
-  Symbols:   811
-  CStrings:  1146
+  UUID: 50FCD3D4-E01E-3768-A03C-4E39F0BD8086
+  Functions: 1310
+  Symbols:   815
+  CStrings:  1148
 
Symbols:
+ _SANDBOX_CHECK_CANONICAL
+ _SANDBOX_CHECK_NO_REPORT
+ __AEGenerateAnnotationsForAuditToken
+ _realpath$DARWIN_EXTSN
CStrings:
+ "%{public}sALLOWING mach_msg with forRecording=true because this process is recording AppleEvents"
+ "%{public}sUnexpected event received from %{public}s while the current process is not recording AppleEvents; discarding it."
+ "%{public}saddAnyFileSchemeStringsURLSandboxExtensions() - type=%c%c%c%c string=%{private}s"
+ "%{public}saddFileExtensionHashForPathForAuditToken: error issuing r/w sandbox extension for %{private}s: %{errno}d/%{public}s"
+ "%{public}saddFileExtensionHashForPathForAuditToken: error issuing r/w sandbox extension for %{private}s: %{errno}d/%{public}s. Trying a r/o extension."
+ "%{public}saddFileExtensionHashForPathForAuditToken: error issuing ro sandbox extension for %{private}s: %{errno}d/%{public}s."
+ "%{public}saddFileExtensionHashForPathForAuditToken: failed to encode extension for %{private}s, token=%{public}s err=%s/%d"
+ "file-read-data"
+ "file-write-data"
- "%{public}s%s - implType=%d type=%c%c%c%c"
- "%{public}sALLOWING mach_msg with kAEDontRecord"
- "%{public}saddFileExtensionHashForPath: error issuing r/w sandbox extension: %{errno}d. Trying a r/o extension."
- "%{public}sconsumeSandboxFileSystemHash: error retrieving extension: %d"
- "AppleEvents failed to encode extension for %s, err=%s/%d"
- "addAnyFileSchemeStringsURLSandboxExtensions"
- "checkForFileTypeDescs"

```
