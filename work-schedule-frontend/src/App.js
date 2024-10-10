import React, { useState } from 'react';
import { Calendar, User, Settings, FileText } from 'lucide-react';

function WorkScheduleSystem() {
  const [view, setView] = useState('employee');
  const [scheduleType, setScheduleType] = useState('monthly');
  
  return (
    <div className="container mx-auto p-4">
      <header className="flex justify-between items-center mb-6">
        <h1 className="text-2xl font-bold">Sistema de Escala de Trabalho</h1>
        <div className="flex space-x-2">
          <button className="px-4 py-2 border rounded flex items-center" onClick={() => setView('employee')}>
            <User className="mr-2 h-4 w-4" /> Funcionário
          </button>
          <button className="px-4 py-2 border rounded flex items-center" onClick={() => setView('admin')}>
            <Settings className="mr-2 h-4 w-4" /> Admin
          </button>
        </div>
      </header>
      
      <div className="mb-6">
        <select 
          className="border rounded px-3 py-2 w-[180px]"
          value={scheduleType} 
          onChange={(e) => setScheduleType(e.target.value)}
        >
          <option value="monthly">Mensal</option>
          <option value="bimonthly">Bimestral</option>
          <option value="quarterly">Trimestral</option>
        </select>
      </div>
      
      {view === 'employee' ? (
        <div>
          <h2 className="text-xl font-semibold mb-4">Minha Escala</h2>
          <table className="w-full border-collapse">
            <thead>
              <tr className="bg-gray-100">
                <th className="border p-2 text-left">Data</th>
                <th className="border p-2 text-left">Tipo</th>
                <th className="border p-2 text-left">Horas</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td className="border p-2">12/10/2024</td>
                <td className="border p-2">Feriado</td>
                <td className="border p-2">8h</td>
              </tr>
              <tr>
                <td className="border p-2">19/10/2024</td>
                <td className="border p-2">Hora Extra</td>
                <td className="border p-2">4h</td>
              </tr>
            </tbody>
          </table>
        </div>
      ) : (
        <div>
          <h2 className="text-xl font-semibold mb-4">Gerenciar Escala</h2>
          <div className="grid grid-cols-2 gap-4 mb-4">
            <button className="px-4 py-2 bg-blue-500 text-white rounded flex items-center justify-center">
              <Calendar className="mr-2 h-4 w-4" /> Gerar Nova Escala
            </button>
            <button className="px-4 py-2 border rounded flex items-center justify-center">
              <FileText className="mr-2 h-4 w-4" /> Exportar CSV
            </button>
          </div>
          <input className="w-full border rounded px-3 py-2 mb-4" placeholder="Buscar funcionário..." />
          <table className="w-full border-collapse">
            <thead>
              <tr className="bg-gray-100">
                <th className="border p-2 text-left">Nome</th>
                <th className="border p-2 text-left">Disciplina</th>
                <th className="border p-2 text-left">Grupo</th>
                <th className="border p-2 text-left">Ações</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td className="border p-2">João Silva</td>
                <td className="border p-2">POS</td>
                <td className="border p-2">A</td>
                <td className="border p-2">
                  <button className="text-blue-500 hover:underline">Editar</button>
                </td>
              </tr>
              <tr>
                <td className="border p-2">Maria Santos</td>
                <td className="border p-2">POS</td>
                <td className="border p-2">B</td>
                <td className="border p-2">
                  <button className="text-blue-500 hover:underline">Editar</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      )}
      
      <div className="mt-6">
        <h3 className="text-lg font-semibold mb-2">Assistente IA</h3>
        <div className="flex space-x-2">
          <input className="flex-grow border rounded px-3 py-2" placeholder="Faça uma pergunta sobre a escala..." />
          <button className="px-4 py-2 bg-green-500 text-white rounded">Perguntar</button>
        </div>
      </div>
    </div>
  );
}

export default WorkScheduleSystem;