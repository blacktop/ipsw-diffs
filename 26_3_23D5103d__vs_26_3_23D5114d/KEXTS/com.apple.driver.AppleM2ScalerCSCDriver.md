## com.apple.driver.AppleM2ScalerCSCDriver

> `com.apple.driver.AppleM2ScalerCSCDriver`

```diff

-154.22.0.0.0
-  __TEXT.__const: 0x6a058
-  __TEXT.__cstring: 0x1b2bf
-  __TEXT_EXEC.__text: 0x105ce0
+154.25.0.0.0
+  __TEXT.__const: 0x6b888
+  __TEXT.__cstring: 0x1b619
+  __TEXT_EXEC.__text: 0x105d54
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1ff08
   __DATA.__common: 0x2330

   __DATA_CONST.__auth_ptr: 0x88
   __DATA_CONST.__mod_init_func: 0x650
   __DATA_CONST.__mod_term_func: 0x5a8
-  __DATA_CONST.__const: 0x24d10
+  __DATA_CONST.__const: 0x24e88
   __DATA_CONST.__kalloc_type: 0x4700
   __DATA_CONST.__kalloc_var: 0xb90
-  UUID: 5730C06C-5BC6-343F-B413-134D315FF221
-  Functions: 8388
+  UUID: E978741D-ABEC-3242-9E77-E1BB9F989BFB
+  Functions: 8389
   Symbols:   0
-  CStrings:  2919
+  CStrings:  2969
 
CStrings:
+ "MSR23 scaler[%d] transformComplete: %u, req: %d prio: %u, need_reset: %d status: %u msrIrqSts: %x\n"
+ "Parse step"
+ "SdSubmit"
+ "[%05X %08X] %03u {%08X %08X} ap ptd write %s"
+ "[%05X %08X] %03u {%08X %08X} dram %s"
+ "[%05X %08X] %03u {%08X %08X} fdrfrmsrc %s"
+ "[%05X %08X] %03u {%08X %08X} ptd %s: 0x%x"
+ "[%05X %08X] %03u {%08X %08X} ptd timesync"
+ "[%05X %08X] %03u {%08X %08X} ring buffer %s"
+ "[%05X %08X] %03u {%08X %08X} tiler %s"
+ "bank count"
+ "bank error"
+ "bank ignore"
+ "bank immediate"
+ "bank normal"
+ "broadcast"
+ "drain / no frame_error"
+ "error ignored"
+ "fdr_0_rd_ptr"
+ "fdr_0_wr_ptr"
+ "fdr_1_rd_ptr"
+ "fdr_1_wr_ptr"
+ "fdr_2_rd_ptr"
+ "fdr_2_wr_ptr"
+ "fdr_3_rd_ptr"
+ "fdr_3_wr_ptr"
+ "fdr_4_rd_ptr"
+ "fdr_4_wr_ptr"
+ "fetch done"
+ "flush_partial_frame"
+ "in_flight_timeout"
+ "invoke"
+ "invoke null txs"
+ "next_frame"
+ "parse_next"
+ "parse_next done"
+ "parse_next unpack"
+ "pop"
+ "pop empty"
+ "pop_thread"
+ "prefetch"
+ "pump_frame_src / next_frame"
+ "pump_frame_src / null thread"
+ "pump_frame_src / step_thread_id"
+ "push"
+ "push_thread"
+ "sdr_rd_ptr"
+ "sdr_wr_ptr"
+ "set_mode_flush (pending_drain_tids)"
+ "submit_free"
+ "supervisor_tick irq"
+ "tile_done_isr"
+ "try_submit_cmd"
+ "try_submit_or_enqueue"
- "MSR23 scaler[%d] transformComplete: %u, frame_id: %u prio: %u, status: %u msrIrqSts: %x\n"
- "[%05X %08X] %03u {%08X %08X} apiodma"
- "[%05X %08X] %03u {%08X %08X} ptd rd"
- "[%05X %08X] %03u {%08X %08X} ptd wr"

```
