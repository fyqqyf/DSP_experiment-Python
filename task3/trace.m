function varargout = trace(varargin)
% TRACE MATLAB code for trace.fig
%      TRACE, by itself, creates a new TRACE or raises the existing
%      singleton*.
%
%      H = TRACE returns the handle to a new TRACE or the handle to
%      the existing singleton*.
%
%      TRACE('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in TRACE.M with the given input arguments.
%
%      TRACE('Property','Value',...) creates a new TRACE or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before trace_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to trace_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help trace

% Last Modified by GUIDE v2.5 17-Sep-2013 16:20:52

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @trace_OpeningFcn, ...
                   'gui_OutputFcn',  @trace_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before trace is made visible.
function trace_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to trace (see VARARGIN)

% Choose default command line output for trace
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes trace wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = trace_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;



function edit1_Callback(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit1 as text
%        str2double(get(hObject,'String')) returns contents of edit1 as a double


% --- Executes during object creation, after setting all properties.
function edit1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit2_Callback(hObject, eventdata, handles)
% hObject    handle to edit2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit2 as text
%        str2double(get(hObject,'String')) returns contents of edit2 as a double


% --- Executes during object creation, after setting all properties.
function edit2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit3_Callback(hObject, eventdata, handles)
% hObject    handle to edit3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit3 as text
%        str2double(get(hObject,'String')) returns contents of edit3 as a double


% --- Executes during object creation, after setting all properties.
function edit3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
t = 0:0.1:100;
%从界面上获取电路参数
R = str2num(get(handles.edit1,'string'));
L = str2num(get(handles.edit2,'string'));
C = str2num(get(handles.edit3,'string'));
%若系统以iL(t)，vc(t)为响应，以e(t)为激励， 
%确定系统状态方程和输出方程中的a,b,c,d矩阵
a = [-R/L -1/L;1/C 0];
b = [1/L;0];
c = [1 0;0 1];
d = [0];sys = ss(a,b,c,d);
sys=ss(a,b,c,d);        %建立系统状态空间模型
Response = step(sys,t); %求系统的阶跃响应
axes(handles.axes1);
plot(t,Response(:,1),'b-','linewidth',3); %显示iL(t)
ylabel('il(t)','fontsize',14)
axes(handles.axes2);
plot(t,Response(:,2),'r-','linewidth',3);%显示vc(t)
ylabel('vc(t)','fontsize',14)
axes(handles.axes3);
plot(Response(:,2),Response(:,1),'linewidth',3); %显示状态轨迹
xlabel('vc(t)','fontsize',14)
ylabel('il(t)','fontsize',14)
%判断系统的阻尼状态
alph = R/(2*L);
omega = 1/sqrt(L*C);
if (R==0)
str = '无阻尼';
else
if(alph>omega)
str = '过阻尼';
end
if(alph==omega)
str = '临界阻尼';
end
if(alph<omega)
str = '欠阻尼';
end
end
set(handles.text1,'string',str);
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)