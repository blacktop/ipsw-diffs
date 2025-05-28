## libRPAC.dylib

> `/usr/lib/libRPAC.dylib`

```diff

-46.0.0.0.0
-  __TEXT.__text: 0x8af90
+55.0.0.0.0
+  __TEXT.__text: 0x8b104
   __TEXT.__auth_stubs: 0x850
   __TEXT.__objc_stubs: 0x180
   __TEXT.__init_offsets: 0x4
-  __TEXT.__cstring: 0x36aa
+  __TEXT.__cstring: 0x364d
   __TEXT.__gcc_except_tab: 0x30
-  __TEXT.__const: 0xe38
+  __TEXT.__const: 0x11c0
   __TEXT.__objc_methname: 0x128
   __TEXT.__oslogstring: 0x1d
   __TEXT.__unwind_info: 0x224

   __DATA_CONST.__const: 0x3d0
   __DATA_CONST.__cfstring: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA.__objc_selrefs: 0x80
-  __DATA.__objc_classrefs: 0x18
   __DATA.__data: 0x7c4
   __DATA.__interpose: 0x90
   __DATA.__common: 0x800e8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 174
-  Symbols:   511
-  CStrings:  417
+  Symbols:   510
+  CStrings:  424
 
Symbols:
+ __ZNSt3__119piecewise_constructE
+ __ZSt28__throw_bad_array_new_lengthB8ue170006v
- __ZNSt3__1L19piecewise_constructE
- __ZSt28__throw_bad_array_new_lengthB7v160006v
CStrings:
+ " waiting on a thread without a QoS class specified "
+ "%s does data processing"
+ "%s is a vision request"
+ "%s reads a database"
+ "%s writes to a database"
+ "%sExpensive vision requests can lead to UI responsiveness issues when executed on main thread. Consider ways to optimize this code path"
+ "%sThis code path does I/O on the main thread underneath that can lead to UI responsiveness issues. Consider ways to optimize this code path"
+ "%sThis code path does data processing on the main thread. Consider ways to optimize this code path"
+ "%sThis code path does interprocess communication underneath which can cause non-deterministic delays. Investigate ways to do this work off the main thread"
+ "%sThis code path may not propagate priority of the main thread when waiting for a signal from another thread. Consider ways to optimize this code path"
+ "%sThis code path may wait on a dispatch semaphore which can cause a priority inversion. Consider ways to optimize this code path"
+ "%sThis code path reads from a database on the main thread. Consider ways to optimize this code path"
+ "%sThis code path writes to a database on the main thread. Consider ways to optimize this code path"
+ "(base priority %d)"
+ "Expensive vision requests can lead to UI responsiveness issues when executed on main thread. Consider ways to optimize this code path"
+ "This code path does I/O on the main thread underneath that can lead to UI responsiveness issues. Consider ways to optimize this code path"
+ "This code path does data processing on the main thread. Consider ways to optimize this code path"
+ "This code path does interprocess communication underneath which can cause non-deterministic delays. Investigate ways to do this work off the main thread"
+ "This code path may not propagate priority of the main thread when waiting for a signal from another thread. Consider ways to optimize this code path"
+ "This code path may wait on a dispatch semaphore which can cause a priority inversion. Consider ways to optimize this code path"
+ "This code path reads from a database on the main thread. Consider ways to optimize this code path"
+ "This code path writes to a database on the main thread. Consider ways to optimize this code path"
+ "VNRequestOnMainThreadAGPCLogType"
+ "computer vision tasks on main thread"
+ "vnrequestonmainthreadagpclogtype"
- " waiting on a thread without a QoS class specified"
- "%s accesses a database underneath which triggers I/O"
- "%s does not propagate thread priority. Consider ways to optimize this code path"
- "%s issues writes to a database underneath which triggers I/O"
- "%s reads a database underneath which triggers I/O"
- "%s%s does not propagate thread priority. Consider ways to optimize this code path"
- "%sCalling %s may result in waiting on a dispatch semaphore which can cause a priority inversion. Consider ways to do this work on a lower QoS thread"
- "%sThis method accesses a database on the main thread underneath which triggers I/O. Inspect the indexing behavior and configuration of your database to optimize this code path"
- "%sThis method does I/O on the main thread underneath that can lead to UI responsiveness issues when called on main thread. Consider ways to optimize this code path"
- "%sThis method does interprocess communication underneath which can cause non-deterministic delays. Investigate ways to do this work off the main thread"
- "%sThis method issues writes to a database on the main thread underneath which triggers I/O. Inspect the indexing behavior and configuration of your database to optimize this code path"
- "%sThis method reads a database on the main thread underneath which triggers I/O. Inspect the indexing behavior and configuration of the database to optimize this code path"
- "Calling %s may result in waiting on a dispatch semaphore which can cause a priority inversion. Consider ways to do this work on a lower QoS thread"
- "This method accesses a database on the main thread underneath which triggers I/O. Inspect the indexing behavior and configuration of your database to optimize this code path"
- "This method does I/O on the main thread underneath that can lead to UI responsiveness issues when called on main thread. Consider ways to optimize this code path"
- "This method does interprocess communication underneath which can cause non-deterministic delays. Investigate ways to do this work off the main thread"
- "This method issues writes to a database on the main thread underneath which triggers I/O. Inspect the indexing behavior and configuration of your database to optimize this code path"
- "This method reads a database on the main thread underneath which triggers I/O. Inspect the indexing behavior and configuration of your database to optimize this code path"

```
