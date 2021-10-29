#
# @VideoConverterModel.py Copyright (c) 2021 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#


class VideoConverterModel:
    """ Video converter, allows you to combine one or two videos from 5 different options """

    def GetCommandsForVideo(self,
                            base_dir: str,
                            sessionkey: str,
                            vf_horizontally: bool,
                            vf_vertically: bool,
                            vf_remove_audio: bool,
                            vf_rotate: bool,
                            vf_percentage: int,
                            vf_reduce_video: bool,
                            input1,
                            input2='') -> str:

        cmd_ffmpeg = 'ffmpeg -i '

        # First output
        output = str(base_dir) + "/media/" + sessionkey + '_output'
        # Final Output
        finaloutput = None

        commands = []

        # 1 Stack two Videos Horizontally
        if vf_horizontally == True:
            cmd = cmd_ffmpeg + input1 + ' -i ' + input2 + ' -filter_complex hstack=inputs=2 ' + output + '.mp4'
            input1 = output + ".mp4"
            finaloutput = output
            output = output + '1'
            commands.append(cmd)

        # 2 Stack two Videos Vertically
        if vf_vertically == True:
            cmd = cmd_ffmpeg + input1 + ' -i ' + input2 + ' -filter_complex vstack=inputs=2 ' + output + '.mp4'
            input1 = output + ".mp4"
            finaloutput = output
            output = output + '2'
            commands.append(cmd)

        # 3 Remove audio from a video
        if vf_remove_audio == True:
            cmd = cmd_ffmpeg + input1 + ' -c:v copy -an ' + output + '.mp4'
            input1 = output + ".mp4"
            finaloutput = output
            output = output + '3'
            commands.append(cmd)

        """ 4 Rotate a video clockwise
              0 = 90 Counter clockwise and Vertical Flip (default)
              1 = 90 Clockwise
              2 = 90 CounterClockwise
              3 = 90 Clockwise and Vertical Flip"""
        if vf_rotate == True:
            if int(vf_percentage) == 2:
                vf_str_percentage = str(vf_percentage)
                cmd = cmd_ffmpeg + input1 + ' -vf "transpose=' + vf_str_percentage + ',' + 'transpose=' + \
                      vf_str_percentage + '" ' + output + '.mp4'
            else:
                vf_str_percentage = str(vf_percentage)
                cmd = cmd_ffmpeg + input1 + ' -vf "transpose=' + vf_str_percentage + '" ' + output + '.mp4'

            input1 = output + ".mp4"
            finaloutput = output
            output = output + '4'
            commands.append(cmd)

        # 5 Reduce the video to 480p
        if vf_reduce_video == True:
            cmd = cmd_ffmpeg + input1 + ' -vf scale=220:240 -preset slow -crf 18 ' + output + '.mp4'
            input1 = output + ".mp4"
            finaloutput = output
            output = output + '5'
            commands.append(cmd)

        # Rename the final file
        if len(commands) > 0:
            commands.append('rename|' + finaloutput.replace('\\', '/') + '.mp4|' + str(base_dir).replace('\\',
                            '/') + "/media/" + sessionkey + '.mp4')
        return commands
