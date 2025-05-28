## IOMFB_bics_daemon

> `/usr/libexec/IOMFB_bics_daemon`

```diff

-337.5.36.0.0
-  __TEXT.__text: 0x847c
-  __TEXT.__auth_stubs: 0x8b0
-  __TEXT.__cstring: 0x2083
+337.7.12.5.0
+  __TEXT.__text: 0x88e8
+  __TEXT.__auth_stubs: 0x8f0
+  __TEXT.__cstring: 0x2176
   __TEXT.__gcc_except_tab: 0xa0
   __TEXT.__const: 0x2b48
-  __TEXT.__unwind_info: 0x248
+  __TEXT.__unwind_info: 0x244
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0x460
+  __DATA_CONST.__auth_got: 0x480
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x420
+  __DATA_CONST.__const: 0x458
   __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__data: 0xa0
+  __DATA.__data: 0x258
   __DATA.__bss: 0x495
   __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libamsupport.dylib
   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 157
-  Symbols:   160
-  CStrings:  367
+  Functions: 161
+  Symbols:   164
+  CStrings:  376
 
Symbols:
+ _BIMUpdaterEndUpdate
+ _BIMUpdaterStartUpdate
+ _mach_absolute_time
+ _mach_timebase_info
CStrings:
+ "BICSSaveYielding"
+ "IOMFB: BIMUpdaterEndUpdate "
+ "IOMFB: BIMUpdaterStartUpdate "
+ "Interrupted by sleep at %s task!!\n"
+ "Task %s took %llu millisec\n"
+ "Tasks completed!!\n"
+ "Unable to begin BIM update"
+ "Unable to end BIM update"
+ "Woke up: resuming pending tasks.\n"

```
