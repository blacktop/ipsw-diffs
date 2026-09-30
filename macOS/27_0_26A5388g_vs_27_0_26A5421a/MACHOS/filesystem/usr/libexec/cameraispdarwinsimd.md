## cameraispdarwinsimd

> `/usr/libexec/cameraispdarwinsimd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`

```diff

-20.57.4.0.0
-  __TEXT.__text: 0x14d48
+20.70.0.0.0
+  __TEXT.__text: 0x14e28
   __TEXT.__auth_stubs: 0xd40
   __TEXT.__init_offsets: 0x4
-  __TEXT.__cstring: 0x19ea
+  __TEXT.__cstring: 0x1a40
   __TEXT.__const: 0x160
   __TEXT.__gcc_except_tab: 0x1dc
-  __TEXT.__oslogstring: 0x22ab
+  __TEXT.__oslogstring: 0x22ef
   __TEXT.__unwind_info: 0x350
   __DATA_CONST.__const: 0x7d80
   __DATA_CONST.__cfstring: 0x5c0

   __DATA_CONST.__auth_got: 0x6a8
   __DATA_CONST.__got: 0xc8
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA.__data: 0x3aebe8
+  __DATA.__data: 0x3bdbe8
   __DATA.__bss: 0xb8
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libz.1.dylib
   Functions: 296
   Symbols:   244
-  CStrings:  399
+  CStrings:  402
 
Functions:
~ sub_100000c58 : 1192 -> 1276
~ sub_10000bc90 -> sub_10000bce4 : 296 -> 324
~ sub_10000c1c0 -> sub_10000c230 : 12 -> 16
~ sub_10000c1cc -> sub_10000c240 : 16 -> 12
~ sub_10000cac4 -> sub_10000cb34 : 2148 -> 2260
CStrings:
+ "/usr/local/share/firmware/isp/0227_01XX.dat"
+ "/usr/local/share/firmware/isp/2226_01XX.dat"
+ "20.70"
+ "ISP still in use by another session; keeping shared interface open\n"
- "20.57.4"
```
