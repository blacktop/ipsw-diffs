## AudioSessionServer

> `/System/Library/PrivateFrameworks/AudioSessionServer.framework/AudioSessionServer`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-449.105.0.0.0
-  __TEXT.__text: 0x6ef6c
+449.107.0.0.0
+  __TEXT.__text: 0x6f430
   __TEXT.__realtime: 0x49c
   __TEXT.__objc_methlist: 0xc4c
-  __TEXT.__gcc_except_tab: 0xa600
-  __TEXT.__const: 0xbf0
-  __TEXT.__cstring: 0x48ff
-  __TEXT.__oslogstring: 0x52a3
+  __TEXT.__gcc_except_tab: 0xa638
+  __TEXT.__const: 0xbd0
+  __TEXT.__cstring: 0x490c
+  __TEXT.__oslogstring: 0x547e
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x2d30
+  __TEXT.__unwind_info: 0x2d48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 1673
-  Symbols:   2754
-  CStrings:  1005
+  Symbols:   2755
+  CStrings:  1014
 
Symbols:
+ __ZN12_GLOBAL__N_131queryHardwareOnlyLatencySamplesEjjPKc
+ __ZN4avas6server18DeviceTimeObserver17setFixedLatenciesEjNSt3__18optionalIjEES4_
+ __ZN4avas6server18DeviceTimeObserver28sessionsObservingDeviceEventEj24AVAudioIOControllerEventbNSt3__18optionalIjEES5_
- __ZN4avas6server18DeviceTimeObserver15setFixedLatencyEjyy
- __ZN4avas6server18DeviceTimeObserver28sessionsObservingDeviceEventEj24AVAudioIOControllerEventb
CStrings:
+ "%25s:%-5d Warning - ignoring btPts that has bad host time: %llu (expected > previousMts i.e.: %llu) (device ID: %u)"
+ "%25s:%-5d Warning - ignoring btPts with negative sample time: %.3f (pts: %.3f)(device ID: %u)"
+ "%25s:%-5d dto device ID: %u has bad sample rate: %f"
+ "%25s:%-5d dto failed to get %s device constant latency (device ID: %u)"
+ "%25s:%-5d dto latency not supported on %s scope (device ID: %u)"
+ "%25s:%-5d dto set fixed input latency: %.2f ms for device ID: %u"
+ "%25s:%-5d dto set fixed output latency: %.2f ms for device ID: %u"
+ "%25s:%-5d dto start event for device ID: %u, supportsDynamicLatency: %d"
+ "%25s:%-5d dto starting BT presentation time poller for device ID: %u)"
+ "%25s:%-5d dto stop event for device ID: %u)"
+ "%25s:%-5d dto stopping BT presentation time poller for device ID: %u)"
+ "%25s:%-5d dto update sample rate: %f for device ID: %u"
+ "input"
+ "output"
- "%25s:%-5d Warning - ignoring btPts has zero/bad PTS! %.5f (sampleTime: %.5f)"
- "%25s:%-5d Warning - ignoring btPts that has bad host time: %llu (expected > previousMts i.e.: %llu)"
- "%25s:%-5d failed to get output device constant latency"
- "%25s:%-5d starting BT presentation time poller for device ID: %u)"
- "%25s:%-5d stopping BT presentation time poller for device ID: %u)"
```
