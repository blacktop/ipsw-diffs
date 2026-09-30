## adc-silenus-v5x.im4p

> `adc-silenus-v5x.im4p`

```diff

 
-  __TEXT.__text: 0xb2f7a0
-  __TEXT.__const: 0x8522b8
-  __TEXT.__cstring: 0xab1ef
+  __TEXT.__text: 0xb2f90c
+  __TEXT.__const: 0x8522ac
+  __TEXT.__cstring: 0xab2ae
   __TEXT.text_env: 0x57888
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0

   __DATA.__mod_init_func: 0x8
   __DATA._rtk_threads: 0x0
   __DATA.__zerofill: 0x5eeaf8
-  UUID: F53163BF-CCEE-317C-9C5A-84E158FE93BA
+  UUID: 4DB4FEE2-CAF5-37E7-A038-1C9DDA3C1993
   Functions: 9851
   Symbols:   0
-  CStrings:  18759
+  CStrings:  18760
 
Functions:
~ sub_32e18 : 22156 -> 22152
~ sub_193b10 -> sub_193b0c : 1800 -> 1816
~ sub_23e870 -> sub_23e87c : 1024 -> 1276
~ sub_23fa08 -> sub_23fb10 : 780 -> 784
~ sub_245448 -> sub_245554 : 920 -> 980
~ sub_50a230 -> sub_50a378 : 9020 -> 9056
~ sub_b2f664 -> sub_b2f7d0 : 316 -> 324
CStrings:
+ "%s: ch %zu syncLeader %zu statsMaster %zu isStreaming %d aeSuspended %d\n"
+ "%s:CmdSuspendAutoResume: autoSuspendMask 0x%x, master_ch %zu, channelsToSuspend 0x%x, slave %zu\n"
+ "%s:ResumeAllSuspendedChannels: channelsToSuspend 0x%x\n"
+ "%s:RunProcess: statsmaster ch %zu added to channelsToSuspend 0x%x\n"
+ "%s:RunProcess:ch%zu fc %2d m %d autoSuspendMask 0x%x, startedSlaveChMask 0x%x, channelsToSuspend 0x%x, AE# %u, %u\n"
+ "21:46:12"
- "%s: ch %zu statsMaster %zu isStreaming %d aeSuspended %d\n"
- "%s:CmdSuspendAutoResume: autoSuspendMask 0x%x, masterCh %zu, slave %zu\n"
- "%s:RunProcess: autoSuspendMask 0x%x, startedSlaveChMask 0x%x, AE# %u, %u\n"
- "23:58:12"
- "Apr 10 2026"

```
