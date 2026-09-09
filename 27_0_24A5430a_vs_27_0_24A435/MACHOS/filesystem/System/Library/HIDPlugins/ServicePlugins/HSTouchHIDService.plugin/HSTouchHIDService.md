## HSTouchHIDService

> `/System/Library/HIDPlugins/ServicePlugins/HSTouchHIDService.plugin/HSTouchHIDService`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__objc_methtype`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_ivar`
- `__DATA.__data`

```diff

 10100.44.0.0.0
-  __TEXT.__text: 0xcfbcc
+  __TEXT.__text: 0xcfc38
   __TEXT.__auth_stubs: 0x1920
   __TEXT.__objc_stubs: 0x7ae0
   __TEXT.__init_offsets: 0x150c

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5287
+  Functions: 5286
   Symbols:   7773
   CStrings:  4199
 
Functions:
~ __ZNSt3__16vectorIN6HSUtil7Encoder8KeyStateENS_9allocatorIS3_EEE6resizeEm : 284 -> 288
- _OUTLINED_FUNCTION_0
~ +[TrackpadHIDEventProcessor nextScrollPhase:anyScroll:] : 36 -> 40
~ __ZNSt3__16vectorIiNS_9allocatorIiEEE6insertENS_11__wrap_iterIPKiEEOi : 464 -> 460
~ __ZNSt3__118__bitset_partitionB9fqe220106INS_17_ClassicAlgPolicyEPiRNS_7greaterIiEEEENS_4pairIT0_bEES7_S7_T1_ : 1044 -> 1040
~ _MTForceConfigGetThresholdsForStage : 16 -> 20
~ __ZNSt3__16vectorI7MTPointNS_9allocatorIS1_EEE6insertENS_11__wrap_iterIPKS1_EERS6_ : 496 -> 492
~ __ZN13MTPathStates_15getCosineThetasENSt3__16vectorI7MTPointNS0_9allocatorIS2_EEEE : 416 -> 420
~ __ZNSt3__118__bitset_partitionB9fqe220106INS_17_ClassicAlgPolicyEPfRNS_7greaterIfEEEENS_4pairIT0_bEES7_S7_T1_ : 1048 -> 1044
~ __ZNSt3__114__split_bufferI7MTPointRNS_9allocatorIS1_EEE12emplace_backIJRKS1_EEEvDpOT_ : 264 -> 268
~ __ZNSt3__16vectorIfNS_9allocatorIfEEE6resizeEm : 284 -> 288
~ __ZNSt3__16vectorIN11HSTPipeline7ContactENS_9allocatorIS2_EEE6resizeEm : 284 -> 288
~ -[HSTHIDEventGenerator _handleContactFrame:] : 3304 -> 3368
~ -[PointerHIDEventProcessor handleChildHIDEvent:previouslyGeneratedEvent:timestamp:momentumInitiationType:canceledMomentumScroll:].cold.1 : 72 -> 84
~ -[PointerHIDEventProcessor handleChildHIDEvent:previouslyGeneratedEvent:timestamp:momentumInitiationType:canceledMomentumScroll:].cold.2 : 72 -> 84
~ -[PointerHIDEventProcessor handleChildHIDEvent:previouslyGeneratedEvent:timestamp:momentumInitiationType:canceledMomentumScroll:].cold.3 : 72 -> 84
~ -[PointerHIDEventProcessor handleChildHIDEvent:previouslyGeneratedEvent:timestamp:momentumInitiationType:canceledMomentumScroll:].cold.4 : 72 -> 84
~ -[PointerHIDEventProcessor handleChildHIDEvent:previouslyGeneratedEvent:timestamp:momentumInitiationType:canceledMomentumScroll:].cold.5 : 72 -> 84
~ -[PointerHIDEventProcessor handleChildHIDEvent:previouslyGeneratedEvent:timestamp:momentumInitiationType:canceledMomentumScroll:].cold.6 : 72 -> 84
CStrings:
+ "[45i]"
- "[44i]"
```
