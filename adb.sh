#!/bin/sh

echo ${uuid}
echo ${ta_path}
# cd ${ta_path}
echo "---生成 Makefile-----"

echo "TA_DEV_KIT_DIR := ../../export-user_ta/
CROSS_COMPILE := arm-linux-gnueabihf-
CFG_TEE_TA_LOG_LEVEL ?= 2" > Makefile

#cd ${ta_path}
sed -i '$a\CPPFLAGS += -DCFG_TEE_TA_LOG_LEVEL=$(CFG_TEE_TA_LOG_LEVEL)' Makefile


echo "BINARY=${uuid}
TA_ROOT := ." >> Makefile

sed -i '$a\include $(TA_DEV_KIT_DIR)/mk/ta_dev_kit.mk \nall: $(BINARY).ta \n$(BINARY).ta: $(BINARY).bin\n	rm -f $@ \n	cat faked_armv7_uta_signed_header.bin $< > $@' Makefile

echo "clean: clean_ta_file
.PHONY: clean_ta_file
clean_ta_file:" >> Makefile

sed -i '$a\	rm -f $(BINARY).ta' Makefile

echo "----Makefile生成完成----"
