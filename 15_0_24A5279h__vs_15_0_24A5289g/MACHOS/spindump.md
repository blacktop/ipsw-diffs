## spindump

> `/usr/sbin/spindump`

```diff

-379.0.0.0.0
-  __TEXT.__text: 0xdec94
+380.0.0.0.0
+  __TEXT.__text: 0xdee20
   __TEXT.__auth_stubs: 0x1450
   __TEXT.__objc_stubs: 0x4820
   __TEXT.__objc_methlist: 0xca4
   __TEXT.__const: 0x2a0
-  __TEXT.__oslogstring: 0x2f145
-  __TEXT.__cstring: 0x189f2
+  __TEXT.__oslogstring: 0x2f381
+  __TEXT.__cstring: 0x18b07
   __TEXT.__objc_classname: 0x146
   __TEXT.__objc_methtype: 0x593
   __TEXT.__gcc_except_tab: 0x30f0
   __TEXT.__objc_methname: 0x47d3
   __TEXT.__unwind_info: 0x13e8
   __DATA_CONST.__auth_got: 0xa38
-  __DATA_CONST.__got: 0x348
+  __DATA_CONST.__got: 0x350
   __DATA_CONST.__const: 0x1f08
-  __DATA_CONST.__cfstring: 0xc3e0
+  __DATA_CONST.__cfstring: 0xc400
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x88

   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2487
-  Symbols:   436
-  CStrings:  2162
+  Functions: 2488
+  Symbols:   437
+  CStrings:  2163
 
Symbols:
+ _TSPDumpOptions_Symbolicate
+ ___kCFBooleanFalse
- _TSPDumpOptions_NoSymbolicate
CStrings:
+ "Parsing microstackshots file, but no dscsym directory provided, so the layout of the dyld shared cache will be unknown. Use the -dscSymDir option to provide a path to a folder containing dscsym files (e.g. logs/olddsc/ in the sysdiagnose where these microstackshots came from)"

```
