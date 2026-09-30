## RawCamera

> `/System/Library/CoreServices/RawCamera.bundle/RawCamera`

```diff

-1738.120.3.0.0
-  __TEXT.__text: 0x1e2d28
-  __TEXT.__auth_stubs: 0x1850
+1752.0.0.0.0
+  __TEXT.__text: 0x1db5ac
+  __TEXT.__auth_stubs: 0x1760
   __TEXT.__objc_methlist: 0x16e4
-  __TEXT.__const: 0x15326
-  __TEXT.__gcc_except_tab: 0x2d438
+  __TEXT.__const: 0x15352
+  __TEXT.__gcc_except_tab: 0x2cab4
   __TEXT.__oslogstring: 0xec0
-  __TEXT.__cstring: 0xee23
+  __TEXT.__cstring: 0xec07
   __TEXT.__dof_RawCamera: 0x8f7
-  __TEXT.__unwind_info: 0xb1d0
+  __TEXT.__unwind_info: 0xb1f0
   __TEXT.__eh_frame: 0x278
   __TEXT.__objc_classname: 0x4b9
-  __TEXT.__objc_methname: 0x3918
-  __TEXT.__objc_methtype: 0xdd3
+  __TEXT.__objc_methname: 0x3768
+  __TEXT.__objc_methtype: 0xbed
   __TEXT.__objc_stubs: 0x2da0
   __DATA_CONST.__got: 0x9b0
-  __DATA_CONST.__const: 0x2a18
+  __DATA_CONST.__const: 0x29b0
   __DATA_CONST.__objc_classlist: 0x1e0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xcf8
   __DATA_CONST.__objc_superrefs: 0xf0
-  __DATA_CONST.__objc_arraydata: 0x3948
-  __AUTH_CONST.__auth_got: 0xc40
-  __AUTH_CONST.__const: 0x35978
+  __DATA_CONST.__objc_arraydata: 0x3978
+  __AUTH_CONST.__auth_got: 0xbc8
+  __AUTH_CONST.__const: 0x35900
   __AUTH_CONST.__cfstring: 0x18080
   __AUTH_CONST.__objc_const: 0x48b0
   __AUTH_CONST.__objc_arrayobj: 0x570

   __AUTH.__thread_bss: 0x18
   __DATA.__objc_ivar: 0x428
   __DATA.__data: 0x20688
-  __DATA.__bss: 0x62e0
+  __DATA.__bss: 0x62c0
   __DATA.__common: 0x4
   __DATA_DIRTY.__objc_data: 0x12c0
   __DATA_DIRTY.__data: 0x48
-  __DATA_DIRTY.__bss: 0x278
+  __DATA_DIRTY.__bss: 0x248
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  UUID: D5535C56-F042-3945-A7F8-37ADBE609B8B
-  Functions: 6433
-  Symbols:   781
-  CStrings:  7487
+  UUID: D32B76CB-690B-3ED3-91B9-2249867053E5
+  Functions: 6447
+  Symbols:   766
+  CStrings:  7482
 
Symbols:
+ _CFAllocatorAllocateTyped
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6resizeEmc
+ __ZNSt3__16localeC1Ev
+ __ZTVNSt3__115basic_streambufIcNS_11char_traitsIcEEEE
- _CFAllocatorAllocate
- _CFArrayAppendValue
- _CFArrayCreateMutable
- _CFArrayGetCount
- _CFArrayGetValueAtIndex
- _CFArrayRemoveValueAtIndex
- _CFDictionaryCreateMutable
- _CFDictionaryGetValue
- _CFDictionaryRemoveValue
- _CFDictionarySetValue
- _CFStringCreateWithFormat
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
- __Znwm
- _dispatch_barrier_async
- _dispatch_barrier_sync
- _getpagesize
- _mach_task_self_
- _vm_purgable_control
CStrings:
+ "9.0 "
+ "MethodV9"
+ "T{CCameraProfile=^^?ii{CMatrix=II{vector<double, std::allocator<double>>=^d^d^d}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d^d}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d^d}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d^d}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d^d}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d^d}}S{CMatrix=II{vector<double, std::allocator<double>>=^d^d^d}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d^d}}},R,N"
+ "{CCameraProfile=^^?ii{CMatrix=II{vector<double, std::allocator<double>>=^d^d^d}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d^d}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d^d}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d^d}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d^d}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d^d}}S{CMatrix=II{vector<double, std::allocator<double>>=^d^d^d}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d^d}}}16@0:8"
+ "{CMatrix=II{vector<double, std::allocator<double>>=^d^d^d}}40@0:8@16Q24Q32"
+ "{CMatrix=II{vector<double, std::allocator<double>>=^d^d^d}}8@?0"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}8@?0"
+ "{vector<double, std::allocator<double>>=^d^d^d}8@?0"
+ "{vector<int, std::allocator<int>>=^i^i^i}8@?0"
+ "{vector<unsigned int, std::allocator<unsigned int>>=^I^I^I}8@?0"
+ "{vector<unsigned short, std::allocator<unsigned short>>=^S^S^S}8@?0"
- "%p"
- "D30"
- "G6"
- "T{CCameraProfile=^^?ii{CMatrix=II{vector<double, std::allocator<double>>=^d^d{__compressed_pair<double *, std::allocator<double>>=^d}}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d{__compressed_pair<double *, std::allocator<double>>=^d}}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d{__compressed_pair<double *, std::allocator<double>>=^d}}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d{__compressed_pair<double *, std::allocator<double>>=^d}}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d{__compressed_pair<double *, std::allocator<double>>=^d}}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d{__compressed_pair<double *, std::allocator<double>>=^d}}}S{CMatrix=II{vector<double, std::allocator<double>>=^d^d{__compressed_pair<double *, std::allocator<double>>=^d}}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d{__compressed_pair<double *, std::allocator<double>>=^d}}}},R,N"
- "Unable to allocate memory. mmap() of %lu bytes failed. Aborting.\n"
- "com.apple.rawcamera.FEVirtualMemory.PointerToInfo"
- "com.apple.rawcamera.FEVirtualMemory.RecycleArray"
- "size=%ld"
- "{CCameraProfile=^^?ii{CMatrix=II{vector<double, std::allocator<double>>=^d^d{__compressed_pair<double *, std::allocator<double>>=^d}}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d{__compressed_pair<double *, std::allocator<double>>=^d}}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d{__compressed_pair<double *, std::allocator<double>>=^d}}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d{__compressed_pair<double *, std::allocator<double>>=^d}}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d{__compressed_pair<double *, std::allocator<double>>=^d}}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d{__compressed_pair<double *, std::allocator<double>>=^d}}}S{CMatrix=II{vector<double, std::allocator<double>>=^d^d{__compressed_pair<double *, std::allocator<double>>=^d}}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d{__compressed_pair<double *, std::allocator<double>>=^d}}}}16@0:8"
- "{CMatrix=II{vector<double, std::allocator<double>>=^d^d{__compressed_pair<double *, std::allocator<double>>=^d}}}40@0:8@16Q24Q32"
- "{CMatrix=II{vector<double, std::allocator<double>>=^d^d{__compressed_pair<double *, std::allocator<double>>=^d}}}8@?0"
- "{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}8@?0"
- "{vector<double, std::allocator<double>>=^d^d{__compressed_pair<double *, std::allocator<double>>=^d}}8@?0"
- "{vector<int, std::allocator<int>>=^i^i{__compressed_pair<int *, std::allocator<int>>=^i}}8@?0"
- "{vector<unsigned int, std::allocator<unsigned int>>=^I^I{__compressed_pair<unsigned int *, std::allocator<unsigned int>>=^I}}8@?0"
- "{vector<unsigned short, std::allocator<unsigned short>>=^S^S{__compressed_pair<unsigned short *, std::allocator<unsigned short>>=^S}}8@?0"

```
