## GNSSPassthroughLib

> `/System/Library/Extensions/AppleSPU.kext/PlugIns/GNSSPassthroughLib.plugin/GNSSPassthroughLib`

```diff

-1014.120.3.0.0
-  __TEXT.__text: 0x1554
+1046.0.1.0.0
+  __TEXT.__text: 0x15bc
   __TEXT.__auth_stubs: 0x2e0
   __TEXT.__const: 0x80
   __TEXT.__gcc_except_tab: 0xac

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: FCC2026A-8431-3EAA-B9A6-0C162F67650B
+  UUID: DA95DF30-FB08-33DE-8973-2596CBC23CEC
   Functions: 59
   Symbols:   91
   CStrings:  12
Symbols:
+ _CFAllocatorAllocateTyped
+ _CFAllocatorReallocateTyped
+ _kIOMainPortDefault
- _CFAllocatorAllocate
- _CFAllocatorReallocate
- _kIOMasterPortDefault
Functions:
~ __ZN15GNSSPassthrough23QueueDataSourceCallbackEPv : 284 -> 320
~ __ZN15GNSSPassthrough5allocEPK13__CFAllocator : 64 -> 80
~ __ZN15GNSSPassthrough24QueueEventSourceCallbackEPv : 284 -> 320
~ _GNSSPassthroughLibFactory : 164 -> 180

```
