## AMPDevicesAgent

> `/System/Library/PrivateFrameworks/AMPDevices.framework/Versions/Current/Support/AMPDevicesAgent`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1.7.0.146.0
-  __TEXT.__text: 0x66a814
-  __TEXT.__auth_stubs: 0x5910
+1.7.0.161.2
+  __TEXT.__text: 0x66b0cc
+  __TEXT.__auth_stubs: 0x5900
   __TEXT.__objc_stubs: 0x8300
   __TEXT.__init_offsets: 0x90
   __TEXT.__objc_methlist: 0x1f34
   __TEXT.__const: 0x85b08
-  __TEXT.__gcc_except_tab: 0x2af60
-  __TEXT.__cstring: 0x604b6
-  __TEXT.__oslogstring: 0x1c3df
+  __TEXT.__gcc_except_tab: 0x2b020
+  __TEXT.__cstring: 0x604e8
+  __TEXT.__oslogstring: 0x1c576
   __TEXT.__objc_methname: 0x8e2b
   __TEXT.__objc_classname: 0x374
   __TEXT.__objc_methtype: 0x28fd
   __TEXT.__unwind_info: 0x12118
   __TEXT.__eh_frame: 0x1b0
-  __DATA_CONST.__const: 0x54008
+  __DATA_CONST.__const: 0x54028
   __DATA_CONST.__cfstring: 0x13e00
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x48

   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__auth_got: 0x2ca0
+  __DATA_CONST.__auth_got: 0x2c98
   __DATA_CONST.__got: 0xec8
   __DATA_CONST.__auth_ptr: 0x198
   __DATA.__objc_const: 0x2268

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 17934
-  Symbols:   1940
-  CStrings:  19814
+  Functions: 17935
+  Symbols:   1939
+  CStrings:  19812
 
Symbols:
- _pthread_kill
CStrings:
+ "**ERROR**: CCP::Startup - Invalid ExecutionState! ccp:%{public}s state:%d"
+ "**ERROR**: ExecOnFiber - inFiberID != mFiberID! ccp:%{public}s inFiberID:%d mFiberID:%d"
+ "**ERROR**: StartupFiber() - Bad fiber state! ccp:%{public}s state:%d "
+ "**ERROR**: StartupFiber() - Invalid FiberID while sleeping! ccp:%{public}s"
+ "1.7.0.161"
+ "13.7.0.161"
+ "AMPDevicesAgent: 1.7.0.161"
+ "Create fiber for %{public}s CCP queue processing."
+ "Waking fiber for %{public}s CCP queue processing."
+ "eCommandActionValue"
+ "mActiveCommand.execCmdOnFiber()"
+ "mFiberID != kInvalidFiberID"
+ "mFiberID == inFiberID"
- "1.7.0.146"
- "13.7.0.146"
- "AMPDevicesAgent: 1.7.0.146"
- "C"
- "CD"
- "CM"
- "IV"
- "IX"
- "L"
- "M"
- "V"
- "X"
- "XC"
- "XL"
- "inFiberID == mFiberID"
```
